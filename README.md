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
  --max-update-gap [MAX_UPDATE_GAP]
                        (seconds) Limit on how long the gap between successful updates can be. If it is
                        more than this the Prometheus metrics are not exposed and and a null MQTT message
                        will be sent.
  --cloud-api-key [CLOUD_API_KEY]
                        The FoxESS Cloud API key to use.
  --cloud-update-freq [CLOUD_UPDATE_FREQ]
                        (seconds) Limit on how frequently we can request updates. If --mqtt is set
                        updates will be sent this often.
  --modbus [MODBUS]     The ModBus address to connect to.
  --modbus-update-freq [MODBUS_UPDATE_FREQ]
                        (seconds) Limit on how frequently we can request updates. If --mqtt is set
                        updates will be sent this often.
```

## Cloud API

To connect via the Cloud API visit https://www.foxesscloud.com/user/center and generate the API key.
Either store the key in the `CLOUD_API_KEY` environment variable, or pass it to `foxessprom` as
`--cloud-api-key APIKEY`.

## Connecting To Modbus

Connecting to your inverter over Modbus will allow you to query data much more frequently, and without the
instability of using the cloud. However, to connect in this way either you or your installer will need
to wire up a modbus to ethernet or wifi module. Please be careful!

The Home Assistent FoxESS Modbus wiki has an [excellent wiring guide](https://github.com/nathanmarlor/foxess_modbus/wiki),
and information on a number of Modbus devices. This application has only been tested with an Elfin EW11.

Once the adapter is connected please set it up with a static ip address, and then pass `--modbus <ip address>` to
`foxessprom`

## Custom Metrics

In addition to reporting the metrics that are provided by the Fox ESS API, `foxessprom` also
calculates four additional metrics - `foxess_pv_generation`, `foxess_battery_charge`,
`foxess_battery_charge` and `foxess_grid_usage`. These attempt to measure the total amount
of energy generated or used. As we can only get the information about the current power every
two minutes these are only estimates.

## Example Metrics

```
# TYPE foxess_cloud_last_update counter
foxess_cloud_last_update{device="ABCDEFG01234567"} 1740085327.645043
# TYPE foxess_cloud_pvPower gauge
foxess_cloud_pvPower{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_pv1Volt gauge
foxess_cloud_pv1Volt{device="ABCDEFG01234567"} 18.0
# TYPE foxess_cloud_pv1Current gauge
foxess_cloud_pv1Current{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_pv1Power gauge
foxess_cloud_pv1Power{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_pv2Volt gauge
foxess_cloud_pv2Volt{device="ABCDEFG01234567"} 3.4
# TYPE foxess_cloud_pv2Current gauge
foxess_cloud_pv2Current{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_pv2Power gauge
foxess_cloud_pv2Power{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_epsPower gauge
foxess_cloud_epsPower{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_epsCurrentR gauge
foxess_cloud_epsCurrentR{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_epsVoltR gauge
foxess_cloud_epsVoltR{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_epsPowerR gauge
foxess_cloud_epsPowerR{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_RCurrent gauge
foxess_cloud_RCurrent{device="ABCDEFG01234567"} 0.7
# TYPE foxess_cloud_RVolt gauge
foxess_cloud_RVolt{device="ABCDEFG01234567"} 249.9
# TYPE foxess_cloud_RFreq gauge
foxess_cloud_RFreq{device="ABCDEFG01234567"} 50.11
# TYPE foxess_cloud_RPower gauge
foxess_cloud_RPower{device="ABCDEFG01234567"} -0.041
# TYPE foxess_cloud_ambientTemperation gauge
foxess_cloud_ambientTemperation{device="ABCDEFG01234567"} 31.6
# TYPE foxess_cloud_invTemperation gauge
foxess_cloud_invTemperation{device="ABCDEFG01234567"} 23.5
# TYPE foxess_cloud_chargeTemperature gauge
foxess_cloud_chargeTemperature{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_batTemperature gauge
foxess_cloud_batTemperature{device="ABCDEFG01234567"} 22.6
# TYPE foxess_cloud_loadsPower gauge
foxess_cloud_loadsPower{device="ABCDEFG01234567"} 0.248
# TYPE foxess_cloud_generationPower gauge
foxess_cloud_generationPower{device="ABCDEFG01234567"} -0.041
# TYPE foxess_cloud_feedinPower gauge
foxess_cloud_feedinPower{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_gridConsumptionPower gauge
foxess_cloud_gridConsumptionPower{device="ABCDEFG01234567"} 0.289
# TYPE foxess_cloud_invBatVolt gauge
foxess_cloud_invBatVolt{device="ABCDEFG01234567"} 157.9
# TYPE foxess_cloud_invBatCurrent gauge
foxess_cloud_invBatCurrent{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_invBatPower gauge
foxess_cloud_invBatPower{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_batChargePower gauge
foxess_cloud_batChargePower{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_batDischargePower gauge
foxess_cloud_batDischargePower{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_batVolt gauge
foxess_cloud_batVolt{device="ABCDEFG01234567"} 157.9
# TYPE foxess_cloud_batCurrent gauge
foxess_cloud_batCurrent{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_meterPower gauge
foxess_cloud_meterPower{device="ABCDEFG01234567"} 0.289
# TYPE foxess_cloud_meterPower2 gauge
foxess_cloud_meterPower2{device="ABCDEFG01234567"} 0.0
# TYPE foxess_cloud_SoC gauge
foxess_cloud_SoC{device="ABCDEFG01234567"} 11.0
# TYPE foxess_cloud_generation counter
foxess_cloud_generation{device="ABCDEFG01234567"} 2853.5
# TYPE foxess_cloud_ResidualEnergy gauge
foxess_cloud_ResidualEnergy{device="ABCDEFG01234567"} 50.0
# TYPE foxess_cloud_energyThroughput gauge
foxess_cloud_energyThroughput{device="ABCDEFG01234567"} 3112.22
# TYPE foxess_modbus_last_update counter
foxess_modbus_last_update{device="ABCDEFG01234567"} 1740085327.811739
# TYPE foxess_modbus_pv1Volt gauge
foxess_modbus_pv1Volt{device="ABCDEFG01234567"} 12.6
# TYPE foxess_modbus_pv1Current gauge
foxess_modbus_pv1Current{device="ABCDEFG01234567"} 0.0
# TYPE foxess_modbus_pv1Power gauge
foxess_modbus_pv1Power{device="ABCDEFG01234567"} 0.0
# TYPE foxess_modbus_pv2Volt gauge
foxess_modbus_pv2Volt{device="ABCDEFG01234567"} 3.4
# TYPE foxess_modbus_pv2Current gauge
foxess_modbus_pv2Current{device="ABCDEFG01234567"} 0.0
# TYPE foxess_modbus_pv2Power gauge
foxess_modbus_pv2Power{device="ABCDEFG01234567"} 0.0
# TYPE foxess_modbus_invBatVolt gauge
foxess_modbus_invBatVolt{device="ABCDEFG01234567"} 157.8
# TYPE foxess_modbus_invBatCurrent gauge
foxess_modbus_invBatCurrent{device="ABCDEFG01234567"} 0.0
# TYPE foxess_modbus_invBatPower gauge
foxess_modbus_invBatPower{device="ABCDEFG01234567"} 0.0
# TYPE foxess_modbus_RVolt gauge
foxess_modbus_RVolt{device="ABCDEFG01234567"} 251.9
# TYPE foxess_modbus_RCurrent gauge
foxess_modbus_RCurrent{device="ABCDEFG01234567"} 0.6
# TYPE foxess_modbus_invPowerP gauge
foxess_modbus_invPowerP{device="ABCDEFG01234567"} -40
# TYPE foxess_modbus_invPowerQ gauge
foxess_modbus_invPowerQ{device="ABCDEFG01234567"} -30
# TYPE foxess_modbus_invPowerS gauge
foxess_modbus_invPowerS{device="ABCDEFG01234567"} 177
# TYPE foxess_modbus_RFreq gauge
foxess_modbus_RFreq{device="ABCDEFG01234567"} 49.86
# TYPE foxess_modbus_epsVoltR gauge
foxess_modbus_epsVoltR{device="ABCDEFG01234567"} 0.0
# TYPE foxess_modbus_epsCurrentR gauge
foxess_modbus_epsCurrentR{device="ABCDEFG01234567"} 0.0
# TYPE foxess_modbus_epsPowerP gauge
foxess_modbus_epsPowerP{device="ABCDEFG01234567"} 0
# TYPE foxess_modbus_epsPowerQ gauge
foxess_modbus_epsPowerQ{device="ABCDEFG01234567"} 0
# TYPE foxess_modbus_epsPowerS gauge
foxess_modbus_epsPowerS{device="ABCDEFG01234567"} 0
# TYPE foxess_modbus_epsFreq gauge
foxess_modbus_epsFreq{device="ABCDEFG01234567"} 0.0
# TYPE foxess_modbus_meterPower gauge
foxess_modbus_meterPower{device="ABCDEFG01234567"} -0.382
# TYPE foxess_modbus_meter2Power gauge
foxess_modbus_meter2Power{device="ABCDEFG01234567"} 0.0
# TYPE foxess_modbus_invTemperation gauge
foxess_modbus_invTemperation{device="ABCDEFG01234567"} 34.3
# TYPE foxess_modbus_ambientTemperation gauge
foxess_modbus_ambientTemperation{device="ABCDEFG01234567"} 23.8
# TYPE foxess_modbus_batVolt gauge
foxess_modbus_batVolt{device="ABCDEFG01234567"} 157.9
# TYPE foxess_modbus_batCurrent gauge
foxess_modbus_batCurrent{device="ABCDEFG01234567"} 0.0
# TYPE foxess_modbus_SoC gauge
foxess_modbus_SoC{device="ABCDEFG01234567"} 11
# TYPE foxess_modbus_ResidualEnergy gauge
foxess_modbus_ResidualEnergy{device="ABCDEFG01234567"} 50
# TYPE foxess_modbus_batTemperature gauge
foxess_modbus_batTemperature{device="ABCDEFG01234567"} 22.8
# TYPE foxess_modbus_batCycleCount gauge
foxess_modbus_batCycleCount{device="ABCDEFG01234567"} 290
# TYPE foxess_modbus_totalPVEnergy gauge
foxess_modbus_totalPVEnergy{device="ABCDEFG01234567"} 2496.7
# TYPE foxess_modbus_todayPVEnergy gauge
foxess_modbus_todayPVEnergy{device="ABCDEFG01234567"} 1.4
# TYPE foxess_modbus_totalChargeEnergy gauge
foxess_modbus_totalChargeEnergy{device="ABCDEFG01234567"} 1650.5
# TYPE foxess_modbus_todayChargeEnergy gauge
foxess_modbus_todayChargeEnergy{device="ABCDEFG01234567"} 4.8
# TYPE foxess_modbus_totalDischargeEnergy gauge
foxess_modbus_totalDischargeEnergy{device="ABCDEFG01234567"} 1482.7
# TYPE foxess_modbus_todayDischargeEnergy gauge
foxess_modbus_todayDischargeEnergy{device="ABCDEFG01234567"} 4.4
# TYPE foxess_modbus_totalFeedInEnergy gauge
foxess_modbus_totalFeedInEnergy{device="ABCDEFG01234567"} 583.2
# TYPE foxess_modbus_todayFeedInEnergy gauge
foxess_modbus_todayFeedInEnergy{device="ABCDEFG01234567"} 0.0
# TYPE foxess_modbus_totalConsumptionEnergy gauge
foxess_modbus_totalConsumptionEnergy{device="ABCDEFG01234567"} 3701.9
# TYPE foxess_modbus_todayConsumptionEnergy gauge
foxess_modbus_todayConsumptionEnergy{device="ABCDEFG01234567"} 13.5
# TYPE foxess_modbus_generation counter
foxess_modbus_generation{device="ABCDEFG01234567"} 2853.5
# TYPE foxess_modbus_todayOutputEnergy gauge
foxess_modbus_todayOutputEnergy{device="ABCDEFG01234567"} 5.1
# TYPE foxess_modbus_totalInputEnergy gauge
foxess_modbus_totalInputEnergy{device="ABCDEFG01234567"} 888.0
# TYPE foxess_modbus_todayInputEnergy gauge
foxess_modbus_todayInputEnergy{device="ABCDEFG01234567"} 5.3
# TYPE foxess_modbus_totalLoadEnergy gauge
foxess_modbus_totalLoadEnergy{device="ABCDEFG01234567"} 5062.5
# TYPE foxess_modbus_todayLoadEnergy gauge
foxess_modbus_todayLoadEnergy{device="ABCDEFG01234567"} 13.2
# TYPE foxess_last_update counter
foxess_last_update {device="ABCDEFG01234567"} 1740085328.338041
# TYPE foxess_pv1Volt gauge
foxess_pv1Volt {device="ABCDEFG01234567"} 12.6
# TYPE foxess_pv1Current gauge
foxess_pv1Current {device="ABCDEFG01234567"} 0.0
# TYPE foxess_pv1Power gauge
foxess_pv1Power {device="ABCDEFG01234567"} 0.0
# TYPE foxess_pv2Volt gauge
foxess_pv2Volt {device="ABCDEFG01234567"} 3.4
# TYPE foxess_pv2Current gauge
foxess_pv2Current {device="ABCDEFG01234567"} 0.0
# TYPE foxess_pv2Power gauge
foxess_pv2Power {device="ABCDEFG01234567"} 0.0
# TYPE foxess_invBatVolt gauge
foxess_invBatVolt {device="ABCDEFG01234567"} 157.8
# TYPE foxess_invBatCurrent gauge
foxess_invBatCurrent {device="ABCDEFG01234567"} 0.0
# TYPE foxess_invBatPower gauge
foxess_invBatPower {device="ABCDEFG01234567"} 0.0
# TYPE foxess_RVolt gauge
foxess_RVolt {device="ABCDEFG01234567"} 251.8
# TYPE foxess_RCurrent gauge
foxess_RCurrent {device="ABCDEFG01234567"} 0.7
# TYPE foxess_invPowerP gauge
foxess_invPowerP {device="ABCDEFG01234567"} -40
# TYPE foxess_invPowerQ gauge
foxess_invPowerQ {device="ABCDEFG01234567"} -29
# TYPE foxess_invPowerS gauge
foxess_invPowerS {device="ABCDEFG01234567"} 177
# TYPE foxess_RFreq gauge
foxess_RFreq {device="ABCDEFG01234567"} 49.86
# TYPE foxess_epsVoltR gauge
foxess_epsVoltR {device="ABCDEFG01234567"} 0.0
# TYPE foxess_epsCurrentR gauge
foxess_epsCurrentR {device="ABCDEFG01234567"} 0.0
# TYPE foxess_epsPowerP gauge
foxess_epsPowerP {device="ABCDEFG01234567"} 0
# TYPE foxess_epsPowerQ gauge
foxess_epsPowerQ {device="ABCDEFG01234567"} 0
# TYPE foxess_epsPowerS gauge
foxess_epsPowerS {device="ABCDEFG01234567"} 0
# TYPE foxess_epsFreq gauge
foxess_epsFreq {device="ABCDEFG01234567"} 0.0
# TYPE foxess_meterPower gauge
foxess_meterPower {device="ABCDEFG01234567"} -0.383
# TYPE foxess_meter2Power gauge
foxess_meter2Power {device="ABCDEFG01234567"} 0.0
# TYPE foxess_invTemperation gauge
foxess_invTemperation {device="ABCDEFG01234567"} 34.3
# TYPE foxess_ambientTemperation gauge
foxess_ambientTemperation {device="ABCDEFG01234567"} 23.8
# TYPE foxess_batVolt gauge
foxess_batVolt {device="ABCDEFG01234567"} 157.9
# TYPE foxess_batCurrent gauge
foxess_batCurrent {device="ABCDEFG01234567"} 0.0
# TYPE foxess_SoC gauge
foxess_SoC {device="ABCDEFG01234567"} 11
# TYPE foxess_ResidualEnergy gauge
foxess_ResidualEnergy {device="ABCDEFG01234567"} 50
# TYPE foxess_batTemperature gauge
foxess_batTemperature {device="ABCDEFG01234567"} 22.8
# TYPE foxess_batCycleCount gauge
foxess_batCycleCount {device="ABCDEFG01234567"} 290
# TYPE foxess_totalPVEnergy gauge
foxess_totalPVEnergy {device="ABCDEFG01234567"} 2496.7
# TYPE foxess_todayPVEnergy gauge
foxess_todayPVEnergy {device="ABCDEFG01234567"} 1.4
# TYPE foxess_totalChargeEnergy gauge
foxess_totalChargeEnergy {device="ABCDEFG01234567"} 1650.5
# TYPE foxess_todayChargeEnergy gauge
foxess_todayChargeEnergy {device="ABCDEFG01234567"} 4.8
# TYPE foxess_totalDischargeEnergy gauge
foxess_totalDischargeEnergy {device="ABCDEFG01234567"} 1482.7
# TYPE foxess_todayDischargeEnergy gauge
foxess_todayDischargeEnergy {device="ABCDEFG01234567"} 4.4
# TYPE foxess_totalFeedInEnergy gauge
foxess_totalFeedInEnergy {device="ABCDEFG01234567"} 583.2
# TYPE foxess_todayFeedInEnergy gauge
foxess_todayFeedInEnergy {device="ABCDEFG01234567"} 0.0
# TYPE foxess_totalConsumptionEnergy gauge
foxess_totalConsumptionEnergy {device="ABCDEFG01234567"} 3701.9
# TYPE foxess_todayConsumptionEnergy gauge
foxess_todayConsumptionEnergy {device="ABCDEFG01234567"} 13.5
# TYPE foxess_generation counter
foxess_generation {device="ABCDEFG01234567"} 2853.5
# TYPE foxess_todayOutputEnergy gauge
foxess_todayOutputEnergy {device="ABCDEFG01234567"} 5.1
# TYPE foxess_totalInputEnergy gauge
foxess_totalInputEnergy {device="ABCDEFG01234567"} 888.0
# TYPE foxess_todayInputEnergy gauge
foxess_todayInputEnergy {device="ABCDEFG01234567"} 5.3
# TYPE foxess_totalLoadEnergy gauge
foxess_totalLoadEnergy {device="ABCDEFG01234567"} 5062.5
# TYPE foxess_todayLoadEnergy gauge
foxess_todayLoadEnergy {device="ABCDEFG01234567"} 13.2
```
