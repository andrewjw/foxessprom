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
from datetime import time
import http.server
import json
import re
from typing import List, Set

from .devices import Devices

PREFIX = "foxess_"

PATH_DEVICE = re.compile(r"/devices/([^/]+)/(force_charge|work_mode)")


class Server(http.server.HTTPServer):
    def __init__(self, args: argparse.Namespace, devices: Devices):
        super().__init__(args.bind, Handler)
        self.args = args
        self.devices = devices


class Handler(http.server.BaseHTTPRequestHandler):
    server: "Server"

    def do_GET(self) -> None:
        if self.path == "/":
            self.send_index()
        elif self.path == "/devices":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps([d.deviceSN for d
                                         in self.server.devices])
                             .encode("utf8"))
        elif self.path.startswith("/devices/"):
            print(self.path.split("/"))
            sn = self.path.split("/")[2]
            if sn not in self.server.devices:
                self.send_error(404)
            elif self.path.endswith("/scheduler"):
                r = self.server.devices[sn].fox_device.get_scheduler()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps(r).encode("utf8"))
        elif self.path == "/metrics":
            self.send_metrics()
        else:
            self.send_error(404)

    def do_POST(self) -> None:
        raw_content_len = self.headers.get('Content-Length')
        if raw_content_len is None:
            self.send_error(400)
            return
        content_len = int(raw_content_len)
        post_body = self.rfile.read(content_len)

        m = PATH_DEVICE.match(self.path)
        if m is None:
            self.send_error(404)
        elif m.group(2) == "force_charge":
            try:
                device = self.server.devices[m.group(1)]
            except IndexError:
                self.send_error(404)
            else:
                j = json.loads(post_body)
                start = time(int(j["start"].split(":")[0]),
                             int(j["start"].split(":")[1]))
                end = time(int(j["end"].split(":")[0]),
                           int(j["end"].split(":")[1]))
                device.fox_device.set_force_charge_time(start, end)
                self.send_response(201)
                self.end_headers()
        elif m.group(2) == "work_mode":
            try:
                device = self.server.devices[m.group(1)]
            except IndexError:
                self.send_error(404)
            else:
                r = device.fox_device.set_work_mode(post_body.decode("utf8"))
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps(r).encode("utf8"))
        else:
            self.send_error(404)

    def do_DELETE(self) -> None:
        m = PATH_DEVICE.match(self.path)
        if m is None:
            self.send_error(404)
        elif m.group(2) == "force_charge":
            try:
                device = self.server.devices[m.group(1)]
            except IndexError:
                self.send_error(404)
            else:
                device.fox_device.disable_force_charge()
                self.send_response(201)
                self.end_headers()
        else:
            self.send_error(404)

    def send_index(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("""
<html>
<head><title>Fox ESS Cloud Prometheus</title></head>
<body>
<h1>Fox ESS Cloud Prometheus</h1>
<p><a href="/metrics">Metrics</a></p>
</body>
</html>""".encode("utf8"))

    def send_metrics(self) -> None:
        metrics_text: List[str] = []

        seen: Set[str] = set()
        for device in self.server.devices.devices:
            metrics = device.get_metrics()
            if metrics is None:
                continue
            for metric, value, is_counter in metrics.get_prometheus_metrics():
                if metric not in seen:
                    metrics_text.append(
                        f"# TYPE {PREFIX + metric} "
                        f"{'counter' if is_counter else 'gauge'}")
                    seen.add(metric)

                metrics_text.append(
                    f"{PREFIX}{metric}"
                    f"{{device=\"{device.deviceSN}\"}} "
                    f"{value}")

        if len(metrics_text) == 0:
            self.send_error(404)
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(("\n".join(metrics_text)).encode("utf8"))


def serve(args: argparse.Namespace,
          devices: Devices) -> None:  # pragma: no cover
    server = Server(args, devices)
    server.serve_forever()
