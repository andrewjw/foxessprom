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

from pymodbus.client import ModbusTcpClient

from ..device import Device
from ..register import Register
from ..register_group import RegisterGroup


def pvPower(registers: List[Dict[str, Union[str, float]]]) \
        -> Dict[str, Union[str, float]]:
    r1, r2 = registers[2]["value"], registers[5]["value"]
    assert isinstance(r1, float) and isinstance(r2, float), (r1, r2)
    return {
        "name": "pvPower",
        "variable": "pvPower",
        "unit": "kW",
        "value": r1 + r2
    }


def batChargePower(registers: List[Dict[str, Union[str, float]]]) \
        -> Dict[str, Union[str, float]]:
    r8 = registers[8]["value"]
    assert isinstance(r8, float), r8
    return {
        "unit": "kW",
        "name": "Charge Power",
        "variable": "batChargePower",
        "value": abs(r8) if r8 < 0 else 0
    }


def batDischargePower(registers: List[Dict[str, Union[str, float]]]) \
        -> Dict[str, Union[str, float]]:
    r8 = registers[8]["value"]
    assert isinstance(r8, float), r8
    return {
        "unit": "kW",
        "name": "Discharge Power",
        "variable": "batDischargePower",
        "value": r8 if r8 > 0 else 0
    }


def gridConsumptionPower(registers: List[Dict[str, Union[str, float]]]) \
        -> Dict[str, Union[str, float]]:
    r21, r22 = registers[21]["value"], registers[22]["value"]
    assert isinstance(r21, float) and isinstance(r22, float), (r21, r22)
    return {
        "name": "GridConsumption Power",
        "variable": "gridConsumptionPower",
        "unit": "kW",
        "value": abs(r21 + r22) if (r21 + r22) < 0 else 0
    }


def feedinPower(registers: List[Dict[str, Union[str, float]]]) \
        -> Dict[str, Union[str, float]]:
    r21, r22 = registers[21]["value"], registers[22]["value"]
    assert isinstance(r21, float) and isinstance(r22, float), (r21, r22)
    return {
        "name": "Feed In Power",
        "variable": "feedinPower",
        "unit": "kW",
        "value": r21 + r22 if (r21 + r22) > 0 else 0
    }


class FoxESSH1(Device):
    REGISTER_GROUPS: List[RegisterGroup] = [
        RegisterGroup(11000, [
            Register("PV1Volt",
                     "pv1Volt",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/10.0,
                     "V"),
            Register("PV1Current",
                     "pv1Current",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/10.0,
                     "A"),
            Register("PV1Power",
                     "pv1Power",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/1000.0,
                     "kW"),
            Register("PV2Volt",
                     "pv2Volt",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/10.0,
                     "V"),
            Register("PV2Current",
                     "pv2Current",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/10.0,
                     "A"),
            Register("PV2Power",
                     "pv2Power",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/1000.0,
                     "kW"),
            Register("InvBatVolt",
                     "invBatVolt",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/10.0,
                     "V"),
            Register("InvBatCurrent",
                     "invBatCurrent",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/10.0,
                     "A"),
            Register("invBatPower",
                     "invBatPower",  # lower case i to match FoxESS Cloud API
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/1000.0,
                     "kW"),
            Register("GridVolt",
                     "RVolt",
                     ModbusTcpClient.DATATYPE.UINT16,
                     lambda v: v/10.0,
                     "V"),
            Register("InvCurrent",
                     "RCurrent",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/10.0,
                     "A"),
            Register("InvPowerP",
                     "invPowerP",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v,
                     "W"),
            Register("InvPowerQ",
                     "invPowerQ",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v,
                     "Var"),
            Register("InvPowerS",
                     "invPowerS",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v,
                     "VA"),
            Register("GridFrequency",
                     "RFreq",
                     ModbusTcpClient.DATATYPE.UINT16,
                     lambda v: v/100,
                     "Hz"),
            Register("EPS-RVolt",
                     "epsVoltR",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/10.0,
                     "V"),
            Register("EPS-RCurrent",
                     "epsCurrentR",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/10.0,
                     "A"),
            Register("EPSPowerP",
                     "epsPowerP",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v,
                     "W"),
            Register("EPSPowerQ",
                     "epsPowerQ",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v,
                     "Var"),
            Register("EPSPowerS",
                     "epsPowerS",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v,
                     "VA"),
            Register("EPSFrequency",
                     "epsFreq",
                     ModbusTcpClient.DATATYPE.UINT16,
                     lambda v: v/100.0,
                     "Hz"),
            Register("MeterPower",
                     "meterPower",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/1000.0,
                     "kW"),
            Register("Meter2Power",
                     "meter2Power",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/1000.0,
                     "kW"),
            Register("Load Power",
                     "loadsPower",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/1000.0,
                     "℃"),
            Register("InvTemperation",
                     "invTemperation",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/10.0,
                     "℃"),
            Register("AmbientTemperature",
                     "ambientTemperation",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/10.0,
                     "℃")
        ], [pvPower,
            batChargePower,
            batDischargePower,
            gridConsumptionPower,
            feedinPower
            ]),
        RegisterGroup(11034, [
            Register("BatVolt",
                     "batVolt",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/10.0,
                     "V"),
            Register("BatCurrent",
                     "batCurrent",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/10.0,
                     "A"),
            Register("SoC",
                     "SoC",
                     ModbusTcpClient.DATATYPE.UINT16,
                     lambda v: v,
                     "%"),
            Register("Battery Residual Energy",
                     "ResidualEnergy",
                     ModbusTcpClient.DATATYPE.UINT16,
                     lambda v: v,
                     "0.01kWh"),
            Register("batTemperature",
                     "batTemperature",
                     ModbusTcpClient.DATATYPE.INT16,
                     lambda v: v/10.0,
                     "℃")
        ]),
        RegisterGroup(11048, [
            Register("BatCycleCount",
                     "batCycleCount",
                     ModbusTcpClient.DATATYPE.UINT16,
                     lambda v: v,
                     ""),
        ]),
        RegisterGroup(11069, [
            Register("TotalPVEnergy",
                     "totalPVEnergy",
                     ModbusTcpClient.DATATYPE.UINT32,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TodayPVEnergy",
                     "todayPVEnergy",
                     ModbusTcpClient.DATATYPE.UINT16,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TotalChargeEnergy",
                     "totalChargeEnergy",
                     ModbusTcpClient.DATATYPE.UINT32,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TodayChargeEnergy",
                     "todayChargeEnergy",
                     ModbusTcpClient.DATATYPE.UINT16,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TotalDischargeEnergy",
                     "totalDischargeEnergy",
                     ModbusTcpClient.DATATYPE.UINT32,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TodayDischargeEnergy",
                     "todayDischargeEnergy",
                     ModbusTcpClient.DATATYPE.UINT16,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TotalFeedInEnergy",
                     "totalFeedInEnergy",
                     ModbusTcpClient.DATATYPE.UINT32,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TodayFeedInEnergy",
                     "todayFeedInEnergy",
                     ModbusTcpClient.DATATYPE.UINT16,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TotalConsumptionEnergy",
                     "totalConsumptionEnergy",
                     ModbusTcpClient.DATATYPE.UINT32,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TodayConsumptionEnergy",
                     "todayConsumptionEnergy",
                     ModbusTcpClient.DATATYPE.UINT16,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TotalOutputEnergy",
                     "generation",
                     ModbusTcpClient.DATATYPE.UINT32,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TodayOutputEnergy",
                     "todayOutputEnergy",
                     ModbusTcpClient.DATATYPE.UINT16,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TotalInputEnergy",
                     "totalInputEnergy",
                     ModbusTcpClient.DATATYPE.UINT32,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TodayInputEnergy",
                     "todayInputEnergy",
                     ModbusTcpClient.DATATYPE.UINT16,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TotalLoadEnergy",
                     "totalLoadEnergy",
                     ModbusTcpClient.DATATYPE.UINT32,
                     lambda v: v/10.0,
                     "kWH"),
            Register("TodayLoadEnergy",
                     "todayLoadEnergy",
                     ModbusTcpClient.DATATYPE.UINT16,
                     lambda v: v/10.0,
                     "kWH"),
        ])
    ]

    def verify(self) -> bool:
        r = self.client.read_input_registers(10000, count=8, device_id=247)
        return self._parse_string(r.registers) == "H1-3.7-E"

    def get_sn(self) -> str:
        r = self.client.read_input_registers(10008, count=8, device_id=247)
        return self._parse_string(r.registers)

    def _parse_string(self, registers: List[int]) -> str:
        r = []
        for reg in registers:
            if reg >> 8 != 0:
                r.append(chr(reg >> 8))
            if reg & 255 != 0:
                r.append(chr(reg & 255))
        return "".join(r)
