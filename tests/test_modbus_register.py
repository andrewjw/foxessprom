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

import unittest

from pymodbus.client import ModbusTcpClient

from foxessprom.modbus.register import Register


class TestModbusRegister(unittest.TestCase):
    def test_register(self) -> None:
        register = Register(name="RegisterName",
                            variable="RegisterVariable",
                            data_type=ModbusTcpClient.DATATYPE.INT32,
                            convert=lambda x: x / 10.0,
                            unit="RegisterUnit")

        self.assertEqual({
            "name": "RegisterName",
            "variable": "RegisterVariable",
            "unit": "RegisterUnit",
            "value": 65537.5
        }, register.convert([10, 15]))
