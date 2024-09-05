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
from typing import Any, Literal, Optional

from .auth import GetAuth

DOMAIN = 'https://www.foxesscloud.com'
KEY = os.environ["FOX_CLOUD_API_KEY"]

REQUEST_TYPES = Literal["get", "post"]


def make_request(method: REQUEST_TYPES,
                 path: str,
                 param: Optional[Any] = None) -> requests.Response:
    url = DOMAIN + path
    headers = GetAuth().get_signature(token=KEY, path=path)

    if method == 'get':
        return requests.get(url=url,
                            params=param,
                            headers=headers)

    elif method == 'post':
        return requests.post(url=url,
                             json=param,
                             headers=headers)
    else:
        raise ValueError('Unsupported request method')
