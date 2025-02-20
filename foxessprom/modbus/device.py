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
from typing import List

from pymodbus.client import ModbusTcpClient

from .device_metrics import DeviceMetrics
from .register_group import RegisterGroup
from ..utils import utcnow


class InvalidDeviceType(Exception):
    pass


class Device:
    REGISTER_GROUPS: List[RegisterGroup]

    def __init__(self, args: argparse.Namespace):
        self.client = ModbusTcpClient(args.modbus)
        self.client.connect()  # type: ignore

        if not self.verify():
            raise InvalidDeviceType()

        self.sn = self.get_sn()

    def verify(self) -> bool:
        raise NotImplementedError()

    def get_sn(self) -> str:
        raise NotImplementedError()

    def get_metrics(self) -> DeviceMetrics:
        start = utcnow()

        metrics = []
        for register_group in self.REGISTER_GROUPS:
            r = self.client.read_input_registers(register_group.base_register,
                                                 register_group.get_size(),
                                                 slave=247)
            metrics.extend(register_group.convert(r.registers))
        print(f"Loaded modbus metrics in {utcnow() - start}")
        return DeviceMetrics(start, metrics)
