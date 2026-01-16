# foxessprom
# Copyright (C) 2025 Andrew Wilkinson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
from datetime import datetime
import time
import threading
from typing import List, Optional, Tuple

from pymodbus.client import ModbusTcpClient

from ..custom_metrics import CustomMetrics
from .modbus_device_metrics import ModbusDeviceMetrics
from .register_group import RegisterGroup
from ..utils import utcnow


class InvalidDeviceType(Exception):
    pass


class Device:
    REGISTER_GROUPS: List[RegisterGroup]

    def __init__(self, args: argparse.Namespace):
        self.client = ModbusTcpClient(args.modbus)
        self.client.connect()  # type: ignore
        self.metrics: Optional[ModbusDeviceMetrics] = None
        self.last_update: Optional[datetime] = None
        self.custom = CustomMetrics()
        self._lock = threading.Lock()
        self._update_frequency = args.modbus_update_freq

        if not self.verify():
            raise InvalidDeviceType()

        self.sn = self.get_sn()

    def verify(self) -> bool:
        raise NotImplementedError()

    def get_sn(self) -> str:
        raise NotImplementedError()

    def get_metrics(self) -> Tuple[ModbusDeviceMetrics, CustomMetrics]:
        with self._lock:
            start = utcnow()
            if (
                self.metrics is not None
                and self.last_update is not None
                and (start - self.last_update).seconds < self._update_frequency
            ):
                return self.metrics, self.custom

            metrics = []
            for register_group in self.REGISTER_GROUPS:
                r = self.client.read_input_registers(
                    register_group.base_register,
                    count=register_group.get_size(),
                    device_id=247,
                )
                if r.isError():
                    self.reset()
                    raise RuntimeError(
                        "Failed to read registers for "
                        f"{register_group.base_register}: {r}"
                    )
                if len(r.registers) < register_group.get_size():
                    self.reset()
                    raise RuntimeError(
                        "Unexpected number of registers "
                        f"for {register_group.base_register}: "
                        f"{len(r.registers)} "
                        f"expected {register_group.get_size()}"
                    )
                metrics.extend(register_group.convert(r.registers))
            print(f"Loaded modbus metrics in {utcnow() - start}")
            self.metrics = ModbusDeviceMetrics(start, metrics)
            self.custom.update(self.metrics)
            self.last_update = start
            return self.metrics, self.custom

    def reset(self) -> None:
        if self.client.is_socket_open():
            self.client.close()  # type: ignore
        time.sleep(30)
        self.client.connect()  # type: ignore
