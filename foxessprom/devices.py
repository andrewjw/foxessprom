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

from typing import Iterator, List

from .device import Device
from .fox_device import FoxDevice


class Devices:
    def __init__(self) -> None:
        self.devices: List[Device] = [
            Device(fox_device) for fox_device
            in FoxDevice.device_list()
        ]

    def __iter__(self) -> Iterator[Device]:
        for device in self.devices:
            yield device

    def __getitem__(self, key: str) -> Device:
        d = [d for d in self.devices if d.deviceSN == key]
        if len(d) == 0:
            raise IndexError(f"No device with serial {key}.")
        else:
            return d[0]
