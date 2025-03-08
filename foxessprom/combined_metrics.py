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

from itertools import chain
from typing import Dict, Iterator, Optional, Tuple, Union

from .custom_metrics import CustomMetrics
from .cloud.cloud_device_metrics import CloudDeviceMetrics
from .modbus.modbus_device_metrics import ModbusDeviceMetrics

COMBINED_METRIC_NAMES = [
    "pvPower",
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
    "ResidualEnergy",
    "batChargePower",
    "batDischargePower",
    "gridConsumptionPower",
    "loadsPower",
    "feedInPower",
]


class CombinedMetrics:
    def __init__(self,
                 cloud: Optional[Tuple[CloudDeviceMetrics, CustomMetrics]],
                 modbus: Optional[Tuple[ModbusDeviceMetrics,
                                        CustomMetrics]]) -> None:
        self.cloud = cloud
        self.modbus = modbus

        self._previous: Dict[str, float] = {}

    def get_prometheus_metrics(self) -> Iterator[Tuple[str, float, bool]]:
        if self.modbus is not None and self.modbus[0].is_valid():
            metrics = chain(self.modbus[0].get_prometheus_metrics(),
                            self.modbus[1].get_prometheus_metrics())
        elif self.cloud is not None and self.cloud[0].is_valid():
            metrics = chain(self.cloud[0].get_prometheus_metrics(),
                            self.cloud[1].get_prometheus_metrics())

        for metric, value, counter in metrics:
            if counter:
                if metric in self._previous and self._previous[metric] > value:
                    value = self._previous[metric]
                self._previous[metric] = value

            yield metric, value, counter

    def to_json(self) -> Dict[str, Union[str, float]]:
        if self.modbus is not None and self.modbus[0].is_valid():
            return self.modbus[0].to_json() | self.modbus[1].to_json()
        elif self.cloud is not None and self.cloud[0].is_valid():
            return self.cloud[0].to_json() | self.cloud[1].to_json()
        else:
            return {}
