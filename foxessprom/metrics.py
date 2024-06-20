# foxessprom
# Copyright (C) 2020 Andrew Wilkinson
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
from threading import Thread
from typing import Union

from .device import Device

DEVICES = Device.device_list()

PREFIX = "foxess_"

IGNORE_DATA = {"runningState", "batStatus", "batStatusV2",
               "currentFault", "currentFaultCount"}

COUNTER_DATA = {"generation"}


class MetricsLoader:
    def __init__(self) -> None:
        self.last_update: Union[datetime, None] = None
        self.stats = None
        self.loading = False

    def metrics(self) -> None:
        if self.last_update is None or \
           (datetime.utcnow() - self.last_update).total_seconds() >= 120:
            if not self.loading:
                self.loading = True
                Thread(target=self._set_metrics).start()

            if self.last_update is not None and \
               (datetime.utcnow() - self.last_update).total_seconds() > 600:
                return None
        return self.stats

    def _set_metrics(self):
        try:
            start = datetime.utcnow()
            self.stats = self._get_metrics()
            self.last_update = start
            print(f"Loaded metrics in {datetime.utcnow() - start}")
        finally:
            self.loading = False

    def _get_metrics(self):
        metric_text = []
        seen = set()
        for device in DEVICES:
            for data in device.real_query():
                if data["variable"] in IGNORE_DATA:
                    continue
                if data["variable"] not in seen:
                    is_counter = data['variable'] in COUNTER_DATA
                    metric_text.append(
                        f"# TYPE {PREFIX + data['variable']} "
                        f"{'counter' if is_counter else 'gauge'}")
                    seen.add(data["variable"])

                metric_text.append(
                    f"{PREFIX}{data['variable']}"
                    f"{{device=\"{device.deviceSN}\"}} "
                    f"{data['value']}")

        return "\n".join(metric_text)
