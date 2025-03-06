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

from datetime import datetime
from typing import Dict, Iterator, List, Optional, Tuple, Union, cast

from ..device_metrics import DeviceMetrics
from ..utils import utcnow

COUNTER_DATA = {"generation"}


PVGENERATION = 0.0


class Metric:
    # {'unit': 'kW', 'name': 'PVPower',
    #  'variable': 'pvPower', 'value': -0.002}
    def __init__(self, data: Dict[str, Union[str, float]]) -> None:
        self.unit: Optional[str] = cast(str, data["unit"]) \
                                   if "unit" in data else None
        self.name: str = cast(str, data["name"])
        self.variable: str = cast(str, data["variable"])
        self.value: Union[str, float] = data["value"]


class ModbusDeviceMetrics(DeviceMetrics):
    def __init__(self,
                 update_time: datetime,
                 data: List[Dict[str, Union[str, float]]]) -> None:
        DeviceMetrics.__init__(self, update_time)
        self.data: List[Metric] = [Metric(d) for d in data]

    def __getitem__(self, key: str) -> Union[str, float]:
        for metric in self.data:
            if metric.variable == key:
                return metric.value
        raise IndexError(f"No variable with name {key}")

    def is_valid(self) -> bool:
        return (utcnow() - self.update_time).total_seconds() < 5 * 60

    def get_prometheus_metrics(self) -> Iterator[Tuple[str, float, bool]]:
        yield ("last_update", self.update_time.timestamp(), True)
        for metric in self.data:
            if isinstance(metric.value, (int, float)):
                yield (metric.variable,
                       metric.value,
                       metric.variable in COUNTER_DATA)

    def to_json(self) -> Dict[str, Union[str, float]]:
        return {m.variable: m.value for m in self.data}
