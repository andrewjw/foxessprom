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

from .device import Device

DEVICES = Device.device_list()

PREFIX = "foxess_"

IGNORE_DATA = {"runningState", "batStatus", "batStatusV2",
               "currentFault", "currentFaultCount"}

COUNTER_DATA = {"generation"}


def metrics():
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
                f"{PREFIX}{data['variable']}{{device=\"{device.deviceSN}\"}} "
                f"{data['value']}")

    return "\n".join(metric_text)
