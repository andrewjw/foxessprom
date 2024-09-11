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

from typing import Dict, Iterator, Optional, Tuple, Union

from .device_metrics import DeviceMetrics


class CustomMetrics:
    def __init__(self) -> None:
        self.last: Optional[DeviceMetrics] = None
        self.pv_generation: float = 0.0
        self.battery_charge: float = 0.0
        self.battery_discharge: float = 0.0
        self.grid_usage: float = 0.0

    def update(self, metrics: DeviceMetrics) -> None:
        if self.last is None:
            self.last = metrics
            return

        time_since = metrics.update_time - self.last.update_time

        if time_since.total_seconds() > 15 * 60:
            self.last = metrics
            return

        self._update_metric("pvPower",
                            "pv_generation",
                            metrics,
                            time_since.total_seconds())
        self._update_metric("batChargePower",
                            "battery_charge",
                            metrics,
                            time_since.total_seconds())
        self._update_metric("batDischargePower",
                            "battery_discharge",
                            metrics,
                            time_since.total_seconds())
        self._update_metric("gridConsumptionPower",
                            "grid_usage",
                            metrics,
                            time_since.total_seconds())

        self.last = metrics

    def get_prometheus_metrics(self) -> Iterator[Tuple[str, float, bool]]:
        yield ("pv_generation", self.pv_generation, True)
        yield ("battery_charge", self.battery_charge, True)
        yield ("battery_discharge", self.battery_discharge, True)
        yield ("grid_usage", self.grid_usage, True)

    def to_json(self) -> Dict[str, Union[str, float]]:
        return {
            "pv_generation": self.pv_generation,
            "battery_charge": self.battery_charge,
            "battery_discharge": self.battery_discharge,
            "grid_usage": self.grid_usage
        }

    def _update_metric(self,
                       foxmetric: str,
                       custom: str,
                       metrics: DeviceMetrics,
                       time_since: float) -> None:
        assert self.last is not None
        current_power = metrics[foxmetric]
        last_power = self.last[foxmetric]
        assert (isinstance(current_power, float)
                or isinstance(current_power, int)) \
               and (isinstance(last_power, float)
                    or isinstance(last_power, int))
        setattr(self,
                custom,
                getattr(self, custom)
                + ((max(0, current_power) + max(0, last_power)) / 2
                   * time_since / 3600))
