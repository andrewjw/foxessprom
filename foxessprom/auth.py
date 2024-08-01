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

import hashlib
import time
from typing import Dict


class GetAuth:
    def get_signature(self, token: str, path: str, lang: str = 'en') \
                     -> Dict[str, str]:
        """
        This function is used to generate a signature consisting of URL, token,
        and timestamp, and return a dictionary containing the signature
        and other information.
            :param token: your key
            :param path:  your request path
            :param lang: language, default is English.
            :return: with authentication header
        """
        timestamp = round(time.time() * 1000)
        signature = fr'{path}\r\n{token}\r\n{timestamp}'

        result = {
            'token': token,
            'lang': lang,
            'timestamp': str(timestamp),
            'signature': self.md5c(text=signature),
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        return result

    @staticmethod
    def md5c(text: str = "", _type: str = "lower") -> str:
        res = hashlib.md5(text.encode(encoding='UTF-8')).hexdigest()
        if _type.__eq__("lower"):
            return res
        else:
            return res.upper()
