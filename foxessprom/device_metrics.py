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
from typing import Dict, Iterator, Tuple, Union


class DeviceMetrics:
    def __init__(self, update_time: datetime) -> None:
        self.update_time = update_time

    def __getitem__(self, key: str) -> Union[str, float]:
        raise NotImplementedError()

    def is_valid(self) -> bool:
        raise NotImplementedError()

    def get_prometheus_metrics(self) -> Iterator[Tuple[str, float, bool]]:
        raise NotImplementedError()

    def to_json(self) -> Dict[str, Union[str, float]]:
        raise NotImplementedError()
