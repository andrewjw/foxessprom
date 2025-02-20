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

from typing import Dict, List, Union

from .register import Register


class RegisterGroup:
    def __init__(self, base_register: int, registers: List[Register]) -> None:
        self.base_register = base_register
        self.registers = registers

    def get_size(self) -> int:
        r = 0
        for register in self.registers:
            r += register.size()
        return r

    def convert(self,
                registers: List[int]) -> List[Dict[str, Union[str, float]]]:
        r = []
        i = 0
        for register in self.registers:
            r.append(register.convert(registers[i:i+register.size()]))
            i += register.size()
        return r
