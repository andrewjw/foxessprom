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

import requests
import os

from .auth import GetAuth

DOMAIN = 'https://www.foxesscloud.com'
KEY = os.environ["FOX_CLOUD_API_KEY"]


def make_request(method, path, param=None):
    url = DOMAIN + path
    headers = GetAuth().get_signature(token=KEY, path=path)

    if method == 'get':
        response = requests.get(url=url,
                                params=param,
                                headers=headers,
                                verify=False)

    elif method == 'post':
        response = requests.post(url=url,
                                 json=param,
                                 headers=headers,
                                 verify=False)
    else:
        raise Exception('request method error')

    return response
