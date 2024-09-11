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
import json
from typing import cast, Dict
import unittest

import requests_mock

from foxessprom.custom_metrics import CustomMetrics
from foxessprom.device_metrics import DeviceMetrics


class TestCustomMetrics(unittest.TestCase):
    def test_device_list(self) -> None:
        data = json.load(open("tests/device_real_query_response.json", "r"))

        first_metrics = DeviceMetrics(datetime(2024, 1, 1, 18, 0),
                                      data["result"][0]["datas"])
        second_metrics = DeviceMetrics(datetime(2024, 1, 1, 18, 2),
                                       data["result"][0]["datas"])

        custom = CustomMetrics()
        custom.update(first_metrics)
        custom.update(second_metrics)

        metrics = cast(Dict[str, float], custom.to_json())

        self.assertAlmostEqual(metrics["pv_generation"], 0.0)
        self.assertAlmostEqual(metrics["battery_charge"], 0.0)
        self.assertAlmostEqual(metrics["battery_discharge"],
                               0.015766666666666665)
        self.assertAlmostEqual(metrics["grid_usage"], 0.0003666666666666666)
