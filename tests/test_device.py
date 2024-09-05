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

import unittest

import requests_mock

from foxessprom.fox_device import FoxDevice


class TestDevice(unittest.TestCase):
    def test_device_list(self) -> None:
        with requests_mock.Mocker() as m:
            m.post('https://www.foxesscloud.com/op/v0/device/list',
                   text=open("tests/device_list_response.json", "r").read())

            devices = FoxDevice.device_list()

            self.assertEqual(1, len(devices))
            self.assertEqual("StationName", devices[0].stationName)
