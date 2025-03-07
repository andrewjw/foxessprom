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

import argparse
import http.server
from itertools import chain
import json
import traceback
from typing import Callable, List, Set

from sentry_sdk import capture_exception

from .combined_metrics import CombinedMetrics
from .cloud import CloudMetrics
from .modbus import ModbusMetrics

PREFIX = "foxess_"
CLOUD = PREFIX + "cloud_"
MODBUS = PREFIX + "modbus_"


def handle_error(func: Callable[["Handler"], None]) \
        -> Callable[["Handler"], None]:
    def r(self: "Handler") -> None:
        try:
            func(self)
        except Exception as e:
            traceback.print_exc()
            capture_exception(e)

            self.send_response(500)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(f"Exception Occurred.\n".encode("utf8"))
    return r


class Server(http.server.HTTPServer):
    def __init__(self, args: argparse.Namespace):
        super().__init__(args.bind, Handler)
        self.args = args
        self.cloud = CloudMetrics(args) \
            if args.cloud_api_key is not None else None
        self.modbus = ModbusMetrics(args) if args.modbus is not None else None


class Handler(http.server.BaseHTTPRequestHandler):
    server: "Server"

    @handle_error
    def do_GET(self) -> None:
        if self.path == "/":
            self.send_index()
        elif self.path == "/devices":
            self.send_response(200)
            self.end_headers()

            if self.server.modbus is not None:
                devices = [d.sn for d in self.server.modbus.devices]
            elif self.server.cloud is not None:
                devices = [d.deviceSN for d in self.server.cloud.devices]
            else:
                devices = []

            self.wfile.write(json.dumps(devices)
                             .encode("utf8"))
        elif self.path == "/metrics":
            self.send_metrics()
        else:
            self.send_error(404)

    def send_index(self) -> None:
        self.send_response(200)
        self.end_headers()
        self.wfile.write("""
<html>
<head><title>Fox ESS Prometheus</title></head>
<body>
<h1>Fox ESS Prometheus</h1>
<p><a href="/metrics">Metrics</a></p>
</body>
</html>""".encode("utf8"))

    def send_metrics(self) -> None:
        metrics_text: List[str] = []

        self.get_cloud_metrics(metrics_text)
        self.get_modbus_metrics(metrics_text)

        clouddevices = \
            {} if self.server.cloud is None \
            else self.server.cloud.get_metrics()
        modbusdevices = \
            {} if self.server.modbus is None \
            else self.server.modbus.get_metrics()
        seen: Set[str] = set()
        for sn in set(clouddevices.keys() | set(modbusdevices.keys())):
            combined = CombinedMetrics(clouddevices[sn], modbusdevices[sn])
            for metric, value, is_counter in combined.get_prometheus_metrics():
                if metric not in seen:
                    metrics_text.append(
                        f"# TYPE {PREFIX + metric} "
                        f"{'counter' if is_counter else 'gauge'}")
                    seen.add(metric)
                metrics_text.append(
                    f"{PREFIX}{metric} "
                    f"{{device=\"{sn}\"}} "
                    f"{value}")

        if len(metrics_text) == 0:
            self.send_error(404)
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(("\n".join(metrics_text)).encode("utf8"))

    def get_cloud_metrics(self, metrics_text: List[str]) -> None:
        if self.server.cloud is None:
            return

        seen: Set[str] = set()
        for device, cmetrics in self.server.cloud.get_metrics().items():
            if cmetrics is None:
                continue
            chained = chain(cmetrics[0].get_prometheus_metrics(),
                            cmetrics[1].get_prometheus_metrics())
            for metric, value, counter in chained:
                if metric not in seen:
                    metrics_text.append(
                        f"# TYPE {CLOUD + metric} "
                        f"{'counter' if counter else 'gauge'}")
                    seen.add(metric)

                metrics_text.append(
                    f"{CLOUD}{metric}"
                    f"{{device=\"{device}\"}} "
                    f"{value}")

    def get_modbus_metrics(self, metrics_text: List[str]) -> None:
        if self.server.modbus is None:
            return

        seen: Set[str] = set()
        for device, mmetrics in self.server.modbus.get_metrics().items():
            if mmetrics is None:
                continue
            chained = chain(mmetrics[0].get_prometheus_metrics(),
                            mmetrics[1].get_prometheus_metrics())
            for metric, value, is_counter in chained:
                if metric not in seen:
                    metrics_text.append(
                        f"# TYPE {MODBUS + metric} "
                        f"{'counter' if is_counter else 'gauge'}")
                    seen.add(metric)

                metrics_text.append(
                    f"{MODBUS}{metric}"
                    f"{{device=\"{device}\"}} "
                    f"{value}")


def serve(args: argparse.Namespace) -> None:  # pragma: no cover
    server = Server(args)
    server.serve_forever()
