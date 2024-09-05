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

from datetime import datetime
from threading import Thread, Lock
from typing import Optional

from .fox_device import FoxDevice
from .device_metrics import DeviceMetrics
from .utils import utcnow


class Device:
    def __init__(self, fox_device: FoxDevice) -> None:
        self.fox_device = fox_device

        self.metrics: Optional[DeviceMetrics] = None
        self.last_update: Optional[datetime] = None
        self.loading = False
        self.lock = Lock()

    def get_metrics(self, block: bool = False) -> Optional[DeviceMetrics]:
        if self.last_update is None or \
           (utcnow() - self.last_update).total_seconds() >= 120:
            with self.lock:
                thread: Optional[Thread] = None
                if not self.loading:
                    self.loading = True
                    thread = Thread(target=self._set_metrics)
                    thread.start()

            if block and thread is not None:
                thread.join()

            if self.last_update is not None and \
               (utcnow() - self.last_update).total_seconds() > 600:
                return None
        return self.metrics

    def _set_metrics(self) -> None:
        try:
            start = utcnow()

            self.metrics = DeviceMetrics(self.fox_device.real_query())

            self.last_update = start
            print(f"Loaded metrics in {utcnow() - start}")
        finally:
            with self.lock:
                self.loading = False

    deviceSN = property(lambda self: self.fox_device.deviceSN)
