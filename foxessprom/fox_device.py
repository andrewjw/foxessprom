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

from typing import Any, List

from .request import make_request


class FoxDevice:
    def __init__(self, data: Any) -> None:
        self.deviceType = data["deviceType"]
        self.hasBattery = data["hasBattery"]
        self.hasPV = data["hasPV"]
        self.stationName = data["stationName"]
        self.moduleSN = data["moduleSN"]
        self.deviceSN = data["deviceSN"]
        self.productType = data["productType"]
        self.stationID = data["stationID"]
        self.status = data["status"]

    def real_query(self) -> Any:
        path = '/op/v0/device/real/query'
        request_param = {'sn': self.deviceSN, 'variables': []}
        response = make_request('post', path, request_param)
        return response.json()["result"][0]["datas"]

    @staticmethod
    def device_list() -> List["FoxDevice"]:
        path = '/op/v0/device/list'

        request_param = {'currentPage': 1, 'pageSize': 500}

        response = make_request('post', path, request_param)

        return [FoxDevice(data) for data in response.json()["result"]["data"]]

    # @staticmethod
    # def device_detail(sn: str):
    #     path = '/op/v0/device/detail'
    #     request_param = {'sn': '60BH37202BFA097'}
    #     response = fr_requests('get', path, request_param)
    #     save_response_data(response, 'device_detail_response.json')
    #     return response

    # @staticmethod
    # def variable_get():
    #     path = '/op/v0/device/variable/get'
    #     response = fr_requests('get', path)
    #     save_response_data(response, 'device_variable_get_response.json')
    #     return response

    # @staticmethod
    # def history_query():
    #     path = '/op/v0/device/history/query'
    #     """get the current millisecond level timestamp"""
    #     end_time = int(time.time() * 1000)
    #     """timestamp 24 hours ago"""
    #     begin_time = end_time - 3600000
    #     request_param = {'sn': 'sn', 'variables': [],
    #                      'begin': begin_time, 'end': end_time}
    #     response = fr_requests('post', path, request_param)
    #     save_response_data(response, 'device_history_query_response.json')
    #     return response

    # @staticmethod
    # def report_query():
    #     path = '/op/v0/device/report/query'
    #     request_param = {"sn": "sn", "year": 2024, "month": 1, 'day': 17,
    #                      "dimension": "day",
    #                      "variables": ["generation", "feedin",
    #                                    "gridConsumption",
    #                                    "chargeEnergyToTal",
    #                                    "dischargeEnergyToTal"]}
    #     response = fr_requests('post', path, request_param)
    #     save_response_data(response, 'device_report_query_response.json')
    #     return response

    # @staticmethod
    # def device_generation():
    #     path = '/op/v0/device/generation'
    #     request_param = {'sn': 'sn'}
    #     response = fr_requests('get', path, request_param)
    #     save_response_data(response, 'device_generation_response.json')
    #     return response

    # @staticmethod
    # def device_bat_soc_get():
    #     path = '/op/v0/device/battery/soc/get'
    #     request_param = {'sn': 'sn'}
    #     response = fr_requests('get', path, request_param)
    #     save_response_data(response, 'device_bat_soc_get_response.json')
    #     return response

    # @staticmethod
    # def device_bat_soc_set():
    #     path = '/op/v0/device/battery/soc/set'
    #     request_param = {'sn': 'sn', 'minSoc': 10, 'minSocOnGrid': 10}
    #     response = fr_requests('post', path, request_param)
    #     save_response_data(response, 'device_bat_soc_set_response.json')
    #     return response

    # @staticmethod
    # def device_bat_force_charge_time_get():
    #     path = '/op/v0/device/battery/forceChargeTime/get'
    #     request_param = {'sn': 'sn'}
    #     response = fr_requests('get', path, request_param)
    #     save_response_data(response,
    #           'device_bat_force_charge_time_get_response.json')
    #     return response

    # @staticmethod
    # def device_bat_force_charge_time_set():
    #     path = '/op/v0/device/battery/forceChargeTime/set'
    #     request_param = {"sn": "sn", "enable1": True, "enable2": False,
    #                      "startTime1": {"hour": 12, "minute": 0},
    #                      "endTime1": {"hour": 14, "minute": 56},
    #                      "startTime2": {"hour": 2, "minute": 0},
    #                      "endTime2": {"hour": 4, "minute": 0}}
    #     """
    #     request_param = {"sn": "sn", "enable1": False, "enable2": False,
    #              "startTime1": {"hour": 11, "minute": 1},
    #              "endTime1": {"hour": 15, "minute": 57},
    #              "startTime2": {"hour": 3, "minute": 1},
    #              "endTime2": {"hour": 5, "minute": 1}}
    #     """
    #     response = fr_requests('post', path, request_param)
    #     save_response_data(response,
    #       'device_bat_force_charge_time_set_response.json')
    #     return response

    # @staticmethod
    # def device_scheduler_get_flag():
    #     path = '/op/v0/device/scheduler/get/flag'
    #     request_param = {'deviceSN': 'sn'}
    #     response = fr_requests('post', path, request_param)
    #     save_response_data(response,
    #       'device_scheduler_get_flag_response.json')
    #     return response

    # @staticmethod
    # def device_scheduler_set_flag():
    #     path = '/op/v0/device/scheduler/set'
    #     request_param = {'deviceSN': 'sn', 'enable': 0}
    #     response = fr_requests('post', path, request_param)
    #     save_response_data(response,
    #       'device_scheduler_set_flag_response.json')
    #     return response

    # @staticmethod
    # def device_scheduler_get():
    #     path = '/op/v0/device/scheduler/get'
    #     request_param = {'deviceSN': 'sn'}
    #     response = fr_requests('post', path, request_param)
    #     save_response_data(response,
    #       'device_scheduler_get_response.json')
    #     return response

    # @staticmethod
    # def device_scheduler_enable():
    #     path = '/op/v0/device/scheduler/enable'
    #     request_param1 = {"deviceSN": "sn",
    #       "groups": [{"enable": 1, "startHour": 0, "startMinute": 0,
    #                   "endHour": 1, "endMinute": 59,
    #                   "workMode": "SelfUse", "minSocOnGrid": 11,
    #                   "fdSoc": 12, "fdPwr": 5001},
    #                  {"enable": 1, "startHour": 2, "startMinute": 1,
    #                   "endHour": 3, "endMinute": 0,
    #                   "workMode": "SelfUse", "minSocOnGrid": 21,
    #                   "fdSoc": 22, "fdPwr": 5002},
    #                  {"enable": 1, "startHour": 3, "startMinute": 1,
    #                   "endHour": 3, "endMinute": 58,
    #                   "workMode": "Feedin", "minSocOnGrid": 31,
    #                   "fdSoc": 32, "fdPwr": 5003},
    #                  {"enable": 1, "startHour": 4, "startMinute": 1,
    #                   "endHour": 4, "endMinute": 58,
    #                   "workMode": "Backup", "minSocOnGrid": 41,
    #                   "fdSoc": 42, "fdPwr": 5004},
    #                  {"enable": 1, "startHour": 5, "startMinute": 1,
    #                   "endHour": 5, "endMinute": 58,
    #                   "workMode": "ForceCharge", "minSocOnGrid": 51,
    #                   "fdSoc": 52, "fdPwr": 5005},
    #                  {"enable": 1, "startHour": 6, "startMinute": 1,
    #                   "endHour": 6, "endMinute": 58,
    #                   "workMode": "ForceDischarge", "minSocOnGrid": 61,
    #                   "fdSoc": 62, "fdPwr": 5006},
    #                  {"enable": 1, "startHour": 7, "startMinute": 0,
    #                   "endHour": 7, "endMinute": 59,
    #                   "workMode": "ForceDischarge", "minSocOnGrid": 71,
    #                   "fdSoc": 72, "fdPwr": 0},
    #                  {"enable": 1, "startHour": 8, "startMinute": 0,
    #                   "endHour": 23, "endMinute": 59,
    #                   "workMode": "ForceDischarge", "minSocOnGrid": 81,
    #                   "fdSoc": 82, "fdPwr": 6000}]}
    #     request_param2 = {"deviceSN": "sn",
    #       "groups": [{"enable": 0, "startHour": 0, "startMinute": 0,
    #                   "endHour": 0, "endMinute": 1,
    #                   "workMode": "ForceCharge", "minSocOnGrid": 10,
    #                   "fdSoc": 0, "fdPwr": 0},
    #                  {"enable": 0, "startHour": 3, "startMinute": 2,
    #                   "endHour": 4, "endMinute": 1,
    #                   "workMode": "ForceCharge", "minSocOnGrid": 22,
    #                   "fdSoc": 23, "fdPwr": 5003},
    #                  {"enable": 0, "startHour": 4, "startMinute": 2,
    #                   "endHour": 4, "endMinute": 59,
    #                   "workMode": "Backup", "minSocOnGrid": 32,
    #                   "fdSoc": 32, "fdPwr": 5004},
    #                  {"enable": 0, "startHour": 5, "startMinute": 2,
    #                   "endHour": 5, "endMinute": 59,
    #                   "workMode": "Feedin", "minSocOnGrid": 42,
    #                   "fdSoc": 42, "fdPwr": 5005},
    #                  {"enable": 0, "startHour": 6, "startMinute": 2,
    #                   "endHour": 6, "endMinute": 59,
    #                   "workMode": "SelfUse", "minSocOnGrid": 52,
    #                   "fdSoc": 52, "fdPwr": 5006},
    #                  {"enable": 0, "startHour": 7, "startMinute": 1,
    #                   "endHour": 7, "endMinute": 59,
    #                   "workMode": "SelfUse", "minSocOnGrid": 62,
    #                   "fdSoc": 62, "fdPwr": 5007},
    #                  {"enable": 0, "startHour": 8, "startMinute": 1,
    #                   "endHour": 8, "endMinute": 3,
    #                   "workMode": "SelfUse", "minSocOnGrid": 72,
    #                   "fdSoc": 72, "fdPwr": 0},
    #                  {"enable": 0, "startHour": 22, "startMinute": 59,
    #                   "endHour": 23, "endMinute": 59,
    #                   "workMode": "SelfUse", "minSocOnGrid": 100,
    #                   "fdSoc": 100, "fdPwr": 6000}]}
    #     response = fr_requests('post', path, request_param2)
    #     save_response_data(response, 'device_scheduler_set_response.json')
    #     return response
