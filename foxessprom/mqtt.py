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
from threading import Thread
import json
import time

import paho.mqtt.publish as publish

from .devices import Devices


def mqtt_updates(args: argparse.Namespace,
                 devices: Devices) -> None:  # pragma: no cover
    if args.mqtt is None:
        return

    Thread(target=_mqtt_update_loop,
           args=(args.mqtt, args.update_limit, devices)).start()


def _mqtt_update_loop(host: str, delay: int, devices: Devices) -> None:
    while True:
        for device in devices:
            metrics = device.get_metrics(block=True)

            publish.single(f"foxess/{device.deviceSN}",
                           json.dumps(
                               metrics.to_json() if metrics is not None
                               else None
                            ),
                           hostname=host)

        time.sleep(delay)
