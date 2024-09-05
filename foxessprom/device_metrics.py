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

from typing import Dict, Iterator, List, Optional, Tuple, Union, cast

PREFIX = "foxess_"

IGNORE_DATA = {"runningState", "batStatus", "batStatusV2",
               "currentFault", "currentFaultCount"}

COUNTER_DATA = {"generation"}


class Metric:
    # {'unit': 'kW', 'name': 'PVPower',
    #  'variable': 'pvPower', 'value': -0.002}
    def __init__(self, data: Dict[str, Union[str, float]]) -> None:
        self.unit: Optional[str] = cast(str, data["unit"]) \
                                   if "unit" in data else None
        self.name: str = cast(str, data["name"])
        self.variable: str = cast(str, data["variable"])
        self.value: Union[str, float] = data["value"]


class DeviceMetrics:
    def __init__(self, data: List[Dict[str, Union[str, float]]]) -> None:
        self.data: List[Metric] = [Metric(d) for d in data]

    def get_prometheus_metrics(self) -> Iterator[Tuple[str, float, bool]]:
        for metric in self.data:
            if isinstance(metric.value, float) \
               and metric.variable not in IGNORE_DATA:
                yield (metric.variable,
                       metric.value,
                       metric.variable in COUNTER_DATA)

    def to_json(self) -> Dict[str, Union[str, float]]:
        return {m.variable: m.value for m in self.data}
