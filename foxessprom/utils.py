# foxessprom
# Copyright (C) 2024 Andrew Wilkinson
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

import datetime
import traceback
from typing import Callable

from sentry_sdk import capture_exception

# TODO: Remove when Python 3.11 is the minimum version.
if hasattr(datetime, "UTC"):
    def utcnow() -> datetime.datetime:
        return datetime.datetime.now(getattr(datetime, "UTC"))
else:
    def utcnow() -> datetime.datetime:
        return datetime.datetime.utcnow()


def capture_errors(func: Callable[[], None]) -> Callable[[], None]:
    def r() -> None:
        try:
            func()
        except Exception as e:
            traceback.print_exception(e)
            capture_exception(e)
    return r
