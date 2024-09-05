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

import argparse
import os
from typing import Sequence

parser = argparse.ArgumentParser(
    description='Reads data from a Fox ESS inverter and PV system, and '
    + 'exposes it as prometheus metrics and MQTT messages.')
parser.add_argument('-q', '--quiet', action="store_true",
                    help="don't log HTTP requests")
parser.add_argument('--bind', type=str, nargs='?', default="0.0.0.0:9100",
                    help='the ip address and port to bind to. Default: *:9100')
parser.add_argument('--mqtt', type=str, nargs='?', default=None,
                    help="the mqtt host to connect to.")
parser.add_argument('--update-limit', type=int, nargs='?', default=120,
                    help="(seconds) Limit on how frequently we can request "
                         + "updates. If --mqtt is set updates will be sent "
                         + "this often.")
parser.add_argument('--max-update-gap', type=int, nargs='?', default=600,
                    help="(seconds) Limit on how long the gap between "
                         + "successful updates can be. If it is more than "
                         + "this the Prometheus metrics are not exposed and "
                         + "and a null MQTT message will be sent.")


def get_arguments(args: Sequence[str]) -> argparse.Namespace:
    parsed_args = parser.parse_args(args)
    if "MQTT_HOST" in os.environ:
        parsed_args.mqtt = os.environ["MQTT_HOST"]

    if ":" not in parsed_args.bind:
        parsed_args.bind = (parsed_args.bind, 9100)
    else:
        parsed_args.bind = (parsed_args.bind.split(":")[0],
                            int(parsed_args.bind.split(":")[1]))

    return parsed_args
