# foxessprom
# Copyright (C) 2024 Andrew Wilkinson
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

from typing import Dict, Iterator, Optional, Tuple, Union

from .cloud.device_metrics import DeviceMetrics as CloudMetrics
from .modbus.device_metrics import DeviceMetrics as ModbusMetrics

COMBINED_METRIC_NAMES = [
    "pv1Volt",
    "pv1Current",
    "pv1Power",
    "pv2Volt",
    "pv2Current",
    "pv2Power",
    "epsCurrentR",
    "epsVoltR",
    "RCurrent",
    "RVolt",
    "RFreq",
    "ambientTemperation",
    "invTemperation",
    "batTemperature",
    "invBatVolt",
    "invBatCurrent",
    "invBatPower",
    "batVolt",
    "batCurrent",
    "meterPower",
    "SoC",
    "ResidualEnergy"
]


class CombinedMetrics:
    def __init__(self,
                 cloud: Optional[CloudMetrics],
                 modbus: Optional[ModbusMetrics]) -> None:
        self.cloud = cloud
        self.modbus = modbus

        self._previous: Dict[str, float] = {}

    def get_prometheus_metrics(self) -> Iterator[Tuple[str, float, bool]]:
        if self.modbus is not None and self.modbus.is_valid():
            metrics = self.modbus.get_prometheus_metrics()
        elif self.cloud is not None and self.cloud.is_valid():
            metrics = self.cloud.get_prometheus_metrics()

        for metric, value, counter in metrics:
            if counter:
                if metric in self._previous and self._previous[metric] > value:
                    value = self._previous[metric]
                self._previous[metric] = value

            yield metric, value, counter

    def to_json(self) -> Dict[str, Union[str, float]]:
        if self.modbus is not None and self.modbus.is_valid():
            return self.modbus.to_json()
        elif self.cloud is not None and self.cloud.is_valid():
            return self.cloud.to_json()
        else:
            return {}
