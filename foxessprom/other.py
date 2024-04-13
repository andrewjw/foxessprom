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

# class Plant:
#     @staticmethod
#     def plant_list():
#         path = '/op/v0/plant/list'
#         request_param = {'currentPage': 1, 'pageSize': 10}
#         response = fr_requests('post', path, request_param)
#         save_response_data(response, 'plant_list_response.json')
#         return response

#     @staticmethod
#     def plant_detail():
#         path = '/op/v0/plant/detail'
#         request_param = {'id': 'abc'}
#         response = fr_requests('get', path, request_param)
#         save_response_data(response, 'plant_detail_response.json')
#         return response

# class Module:
#     @staticmethod
#     def module_list():
#         path = '/op/v0/module/list'

#         request_param = {'currentPage': 1, 'pageSize': 10}

#         response = fr_requests('post', path, request_param)

#         save_response_data(response, 'module_list_response.json')

#         return response

# class User:
#     @staticmethod
#     def user_get_access_count():
#         path = '/op/v0/user/getAccessCount'

#         response = fr_requests('get', path)

#         save_response_data(response, 'user_get_access_count_response.json')

#         return response
