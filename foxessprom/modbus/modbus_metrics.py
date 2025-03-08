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
import threading
import time
from typing import Dict, Optional, Tuple

from ..custom_metrics import CustomMetrics
from .devices import FoxESSH1
from .modbus_device_metrics import ModbusDeviceMetrics
from ..utils import capture_errors, utcnow


class ModbusMetrics:
    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args
        self.device = FoxESSH1(args)
        self.devices = [self.device]

        threading.Thread(target=capture_errors(self._update_loop)).start()

    def get_metrics(self) -> \
            Dict[str, Optional[Tuple[ModbusDeviceMetrics, CustomMetrics]]]:
        metrics = self.device.get_metrics()

        if (utcnow() - metrics[0].update_time).seconds \
                > self.args.max_update_gap:
            return {}

        return {self.device.sn: metrics}

    def _update_loop(self) -> None:
        while True:
            self.device.get_metrics()

            time.sleep(self.args.modbus_update_freq)
