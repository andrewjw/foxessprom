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

from typing import Callable, Dict, List, Union

from pymodbus.client import ModbusTcpClient


class Register:
    def __init__(self,
                 name: str,
                 variable: str,
                 data_type: ModbusTcpClient.DATATYPE,
                 convert: Callable[[Union[int, float]], Union[int, float]],
                 unit: str) -> None:
        self.name = name
        self.variable = variable
        self.data_type = data_type
        self.convert_func = convert
        self.unit = unit

    def size(self) -> int:
        return self.data_type.value[1]

    def convert(self,
                value: List[int]) -> Dict[str, Union[str, int, float]]:
        register_value = \
            ModbusTcpClient.convert_from_registers(value,
                                                   data_type=self.data_type)
        if isinstance(register_value, list):
            raise ValueError(
                f"Register {self.name} ({self.variable}) returned a list, "
                "which is not supported by this implementation. "
                f"{value} -> {register_value}")
        return {
            "unit": self.unit,
            "name": self.name,
            "variable": self.variable,
            "value": register_value if isinstance(register_value, str)
            else self.convert_func(register_value)
        }
