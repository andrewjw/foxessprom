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

from datetime import datetime
import http.server

from .metrics import metrics


LAST_UPDATE = None
STATS = None


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
        global STATS, LAST_UPDATE
        if LAST_UPDATE is None or \
           (datetime.utcnow() - LAST_UPDATE).total_seconds() > 120:
            start = datetime.utcnow()
            STATS = metrics()
            LAST_UPDATE = datetime.utcnow()
            print("Updated metrics in {LAST_UPDATE - start)")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(STATS.encode("utf8"))


def serve():  # pragma: no cover
    server = http.server.HTTPServer(("0.0.0.0", 9100), Handler)
    server.serve_forever()
