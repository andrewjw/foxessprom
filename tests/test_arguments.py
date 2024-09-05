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

import os
import unittest

import requests_mock

from foxessprom.arguments import get_arguments


class TestArguments(unittest.TestCase):
    def test_bind_ip_only(self) -> None:
        args = get_arguments(["--bind", "192.168.1.2"])

        self.assertEqual(("192.168.1.2", 9100), args.bind)

    def test_bind_with_port(self) -> None:
        args = get_arguments(["--bind", "192.168.1.2:9102"])

        self.assertEqual(("192.168.1.2", 9102), args.bind)

    def test_mqtt_variable(self) -> None:
        os.environ["MQTT_HOST"] = "mqtt_host"
        try:
            args = get_arguments([])

            self.assertEqual("mqtt_host", args.mqtt)
        finally:
            del os.environ["MQTT_HOST"]
