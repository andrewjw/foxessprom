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

from .custom_metrics import CustomMetrics
from .device_metrics import DeviceMetrics


class CombinedMetrics:
    def __init__(self,
                 device: Optional[DeviceMetrics],
                 custom: CustomMetrics) -> None:
        self.device = device
        self.custom = custom

    def get_prometheus_metrics(self) -> Iterator[Tuple[str, float, bool]]:
        if self.device is not None:
            for metric in self.device.get_prometheus_metrics():
                yield metric
        for metric in self.custom.get_prometheus_metrics():
            yield metric

    def to_json(self) -> Dict[str, Union[str, float]]:
        # TODO: Use when Python 3.9 is the minimum version
        # return self.device.to_json() if self.device is not None \
        #       else {} | self.custom.to_json()
        return {**(self.device.to_json() if self.device is not None else {}),
                **self.custom.to_json()}
