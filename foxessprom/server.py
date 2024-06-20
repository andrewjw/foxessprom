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

import http.server

from .metrics import MetricsLoader

METRICS = MetricsLoader()


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_index()
        elif self.path == "/metrics":
            self.send_metrics()
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

    def send_metrics(self):
        stats = METRICS.metrics()
        if stats is None:
            self.send_error(404)
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(stats.encode("utf8"))


def serve():  # pragma: no cover
    server = http.server.HTTPServer(("0.0.0.0", 9100), Handler)
    server.serve_forever()
