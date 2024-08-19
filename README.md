[![Pipeline](https://github.com/andrewjw/foxessprom/actions/workflows/build.yaml/badge.svg)](https://github.com/andrewjw/foxessprom/actions/workflows/build.yaml)
[![PyPI version](https://badge.fury.io/py/foxessprom.svg)](https://pypi.org/project/foxessprom/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/foxessprom)](https://pypi.org/project/foxessprom/)
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/andrewjw/foxessprom)](https://hub.docker.com/r/andrewjw/foxessprom)
[![Docker Pulls](https://img.shields.io/docker/pulls/andrewjw/foxessprom)](https://hub.docker.com/r/andrewjw/foxessprom)
[![Coverage Status](https://coveralls.io/repos/github/andrewjw/foxessprom/badge.svg?branch=main)](https://coveralls.io/github/andrewjw/foxessprom?branch=main)

Prometheus exporter for Fox ESS Inverters (using the Fox Cloud API)

## Command Line

```
usage: foxessprom [-h] [-q] [--bind [BIND]] [--mqtt [MQTT]] [--update-limit [UPDATE_LIMIT]] [--max-update-gap [MAX_UPDATE_GAP]]

Reads data from a Fox ESS inverter and PV system, and exposes it as prometheus metrics and MQTT messages.

options:
  -h, --help            show this help message and exit
  -q, --quiet           don't log HTTP requests
  --bind [BIND]         the ip address and port to bind to. Default: *:9100
  --mqtt [MQTT]         the mqtt host to connect to.
  --update-limit [UPDATE_LIMIT]
                        (seconds) Limit on how frequently we can request updates. If --mqtt updates will be sent this often.
  --max-update-gap [MAX_UPDATE_GAP]
                        (seconds) Limit on how long the gap between successful updates can be. If it is more than this the Prometheus metrics are not exposed and a null MQTT message will be sent.
```

## Example Metrics

```
# TYPE foxess_pvPower gauge
foxess_pvPower{device="ABCDEFG01234567"} 0.0
# TYPE foxess_pv1Volt gauge
foxess_pv1Volt{device="ABCDEFG01234567"} 118.4
# TYPE foxess_pv1Current gauge
foxess_pv1Current{device="ABCDEFG01234567"} 0.0
# TYPE foxess_pv1Power gauge
foxess_pv1Power{device="ABCDEFG01234567"} 0.0
# TYPE foxess_pv2Volt gauge
foxess_pv2Volt{device="ABCDEFG01234567"} 122.1
# TYPE foxess_pv2Current gauge
foxess_pv2Current{device="ABCDEFG01234567"} 0.0
# TYPE foxess_pv2Power gauge
foxess_pv2Power{device="ABCDEFG01234567"} 0.0
# TYPE foxess_epsPower gauge
foxess_epsPower{device="ABCDEFG01234567"} -0.001
# TYPE foxess_epsCurrentR gauge
foxess_epsCurrentR{device="ABCDEFG01234567"} 0.0
# TYPE foxess_epsVoltR gauge
foxess_epsVoltR{device="ABCDEFG01234567"} 0.0
# TYPE foxess_epsPowerR gauge
foxess_epsPowerR{device="ABCDEFG01234567"} -0.001
# TYPE foxess_RCurrent gauge
foxess_RCurrent{device="ABCDEFG01234567"} 1.6
# TYPE foxess_RVolt gauge
foxess_RVolt{device="ABCDEFG01234567"} 248.0
# TYPE foxess_RFreq gauge
foxess_RFreq{device="ABCDEFG01234567"} 49.92
# TYPE foxess_RPower gauge
foxess_RPower{device="ABCDEFG01234567"} 0.375
# TYPE foxess_ambientTemperation gauge
foxess_ambientTemperation{device="ABCDEFG01234567"} 43.5
# TYPE foxess_invTemperation gauge
foxess_invTemperation{device="ABCDEFG01234567"} 35.8
# TYPE foxess_chargeTemperature gauge
foxess_chargeTemperature{device="ABCDEFG01234567"} 0.0
# TYPE foxess_batTemperature gauge
foxess_batTemperature{device="ABCDEFG01234567"} 32.5
# TYPE foxess_loadsPower gauge
foxess_loadsPower{device="ABCDEFG01234567"} 0.397
# TYPE foxess_generationPower gauge
foxess_generationPower{device="ABCDEFG01234567"} 0.375
# TYPE foxess_feedinPower gauge
foxess_feedinPower{device="ABCDEFG01234567"} 0.0
# TYPE foxess_gridConsumptionPower gauge
foxess_gridConsumptionPower{device="ABCDEFG01234567"} 0.0
# TYPE foxess_invBatVolt gauge
foxess_invBatVolt{device="ABCDEFG01234567"} 158.9
# TYPE foxess_invBatCurrent gauge
foxess_invBatCurrent{device="ABCDEFG01234567"} 2.5
# TYPE foxess_invBatPower gauge
foxess_invBatPower{device="ABCDEFG01234567"} 0.409
# TYPE foxess_batChargePower gauge
foxess_batChargePower{device="ABCDEFG01234567"} 0.0
# TYPE foxess_batDischargePower gauge
foxess_batDischargePower{device="ABCDEFG01234567"} 0.409
# TYPE foxess_batVolt gauge
foxess_batVolt{device="ABCDEFG01234567"} 159.1
# TYPE foxess_batCurrent gauge
foxess_batCurrent{device="ABCDEFG01234567"} -2.7
# TYPE foxess_meterPower gauge
foxess_meterPower{device="ABCDEFG01234567"} 0.0
# TYPE foxess_meterPower2 gauge
foxess_meterPower2{device="ABCDEFG01234567"} 0.0
# TYPE foxess_SoC gauge
foxess_SoC{device="ABCDEFG01234567"} 89.0
# TYPE foxess_generation counter
foxess_generation{device="ABCDEFG01234567"} 826.5
# TYPE foxess_ResidualEnergy gauge
foxess_ResidualEnergy{device="ABCDEFG01234567"} 471.0
# TYPE foxess_energyThroughput gauge
foxess_energyThroughput{device="ABCDEFG01234567"} 692.866
```
