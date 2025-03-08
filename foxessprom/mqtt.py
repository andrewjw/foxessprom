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
from typing import Optional

import paho.mqtt.publish as publish

from .combined_metrics import CombinedMetrics
from .cloud import CloudMetrics
from .modbus import ModbusMetrics
from .utils import capture_errors


def mqtt_updates(args: argparse.Namespace,
                 cloud: Optional[CloudMetrics],
                 modbus: Optional[ModbusMetrics]) -> None:  # pragma: no cover
    if args.mqtt is None:
        return

    if modbus is not None:
        delay = args.modbus_update_freq
    elif cloud is not None:
        delay = args.cloud_update_freq
    else:
        delay = args.max_update_gap

    Thread(target=capture_errors(
                     lambda:
                     _mqtt_update_loop(
                         args.mqtt,
                         delay,
                         cloud,
                         modbus)
          )).start()


def _mqtt_update_loop(host: str,
                      delay: int,
                      cloud: Optional[CloudMetrics],
                      modbus: Optional[ModbusMetrics]) -> None:
    while True:
        clouddevices = {} if cloud is None else cloud.get_metrics()
        modbusdevices = {} if modbus is None else modbus.get_metrics()

        for sn in set(clouddevices.keys() | set(modbusdevices.keys())):
            combined = CombinedMetrics(clouddevices.get(sn),
                                       modbusdevices.get(sn))

            publish.single(f"foxess/{sn}",
                           json.dumps(combined.to_json()),
                           hostname=host)

        time.sleep(delay)
