# CHANGELOG

<!-- version list -->

## v2.1.0 (2026-01-16)

### Features

- Add support for Python 3.14.
  ([`d91621c`](https://github.com/andrewjw/foxessprom/commit/d91621ca95f27460cf9855f8cd3e4ac8a591791d))


## v2.0.4 (2025-12-11)

### Bug Fixes

- Trim overlong dash prefix of ---cloud-update-frequency flag.
  ([`eac8697`](https://github.com/andrewjw/foxessprom/commit/eac8697366a3a040a04b9685bd22792813160ce5))

### Chores

- Allow submitting coverage data to fail.
  ([`d1ce80a`](https://github.com/andrewjw/foxessprom/commit/d1ce80a384a43900617d44157c9b288a7e647afb))

- Support parallel code coverage submission across Python versions.
  ([`a15366a`](https://github.com/andrewjw/foxessprom/commit/a15366ada54645efb77273c0937ae97d270af81c))

- Update GitHub workflow and PyPI spec to support Python 3.13.
  ([`8169121`](https://github.com/andrewjw/foxessprom/commit/8169121639a3bf8886b44ed5db74b27315c70db4))

- Update parameter names for PyModBus 3.10.0
  ([`638507d`](https://github.com/andrewjw/foxessprom/commit/638507d907cc695d8ea29a9ea767a8e300ab3aee))


## v2.0.3 (2025-06-21)

### Bug Fixes

- Detect if there was an error talking to the modbus device and reconnect.
  ([`0579ab8`](https://github.com/andrewjw/foxessprom/commit/0579ab8c0f565dcdef20ac45a7da42f62474717a))


## v2.0.2 (2025-06-18)

### Bug Fixes

- Fix exception type and show more details when failing to convert a modbus register.
  ([`835ba64`](https://github.com/andrewjw/foxessprom/commit/835ba64e19a60e37a6ec3b581685cbee12b88687))


## v2.0.1 (2025-05-29)

### Bug Fixes

- Fake commit to trigger tag with new pymodbus version.
  ([`87d1d9f`](https://github.com/andrewjw/foxessprom/commit/87d1d9f196022b74374615aaaa4616482514950c))

### Chores

- Update to follow pymodbus api changes.
  ([`3ffa99f`](https://github.com/andrewjw/foxessprom/commit/3ffa99f309c9a282e8902073d6491dd719825dc0))


## v2.0.0 (2025-05-29)

### Features

- Drop support for Python 3.9 as pymodbus has already dropped support.
  ([`59a21c5`](https://github.com/andrewjw/foxessprom/commit/59a21c53a5ba6f9e8bdae9bfc51d662c7a44d623))

### Breaking Changes

- Dropped support for Python 3.9


## v1.1.0 (2025-03-08)

### Bug Fixes

- Fix computed modbus variables.
  ([`ca505c6`](https://github.com/andrewjw/foxessprom/commit/ca505c6571a67d3ef093dfe3dec06ce25785f2b8))

- Fix scaling for modbus loads value.
  ([`7dddce1`](https://github.com/andrewjw/foxessprom/commit/7dddce14db7cccdfe26b94c5454be197b7df6306))

### Features

- Restore mqtt publishing, and enable regular updates to allow custom metrics to be updated without
  web requests.
  ([`ecce4a8`](https://github.com/andrewjw/foxessprom/commit/ecce4a8b96bd201952f8c31fb2a56f3c8b1ce9a7))


## v1.0.1 (2025-03-07)

### Bug Fixes

- Fix serial number not being in both cloud and modbus data.
  ([`34cb728`](https://github.com/andrewjw/foxessprom/commit/34cb728fd10b4916fe976bdb5ebf339228eb3efb))


## v1.0.0 (2025-03-07)

### Chores

- Fix traceback type errors.
  ([`41315d6`](https://github.com/andrewjw/foxessprom/commit/41315d655870b8e35665747af12eab7915d5a436))

- Fix type syntax for Python 3.9
  ([`9675d92`](https://github.com/andrewjw/foxessprom/commit/9675d92fa152487771b1163b9e946b200bc3d7ab))

- Remove type ignore comment.
  ([`5d3acfc`](https://github.com/andrewjw/foxessprom/commit/5d3acfc99dcecec5c946c3fee14092d11fc923c0))

### Features

- Add basic support for getting data from modbus
  ([`04b4616`](https://github.com/andrewjw/foxessprom/commit/04b46165b559f709bcb18f4266c2ba7f88eee849))

- Add support for combining modbus and cloud metrics.
  ([`08b337f`](https://github.com/andrewjw/foxessprom/commit/08b337f5243f0c162a4a895bd9762863a2236cae))

- Add support for error tracking with Sentry.io.
  ([`8836b3a`](https://github.com/andrewjw/foxessprom/commit/8836b3a93c98f731745c3b1c5531dd1ddade8e43))

- Drop support for Python 3.8 as it's end of life.
  ([`6e9d463`](https://github.com/andrewjw/foxessprom/commit/6e9d46317db68d4c80e42ad47b3dbcfbf4e2f568))


## v0.4.3 (2024-10-14)

### Bug Fixes

- Raise error if we get a bad status from the API.
  ([`2064af2`](https://github.com/andrewjw/foxessprom/commit/2064af2af83bc7ba31dba4ee67935b9c9a867d2e))


## v0.4.2 (2024-09-12)

### Bug Fixes

- Add custom total metric for load
  ([`17bee03`](https://github.com/andrewjw/foxessprom/commit/17bee039d9bf2f5f499563aa7cc460860742efb5))


## v0.4.1 (2024-09-11)

### Bug Fixes

- Add total feed in custom metric.
  ([`3bf72b6`](https://github.com/andrewjw/foxessprom/commit/3bf72b622daae1abf65b51ec2dbb186f91c551c6))

- Fix custom metric names to match Prometheus standards.
  ([`4e1c13f`](https://github.com/andrewjw/foxessprom/commit/4e1c13f64c06a6d7486661689f510e38f7a017ff))

### Chores

- Fix tests.
  ([`7e3d112`](https://github.com/andrewjw/foxessprom/commit/7e3d112506bb8a1fa44636815a6983f3b7f698e0))


## v0.4.0 (2024-09-11)

### Chores

- Remove dictionary union to restore Python 3.8 compatibility.
  ([`fccd5b1`](https://github.com/andrewjw/foxessprom/commit/fccd5b18fac3d7f8aefaeff10088dcf1016b8105))

### Features

- Add four new custom metrics to measure the total amount of energy generated or used.
  ([`2d0cc8f`](https://github.com/andrewjw/foxessprom/commit/2d0cc8fdffe9e7e0548a9cf90496ba0c5d49d04d))


## v0.3.1 (2024-09-05)

### Bug Fixes

- Remove deprecated usage of datetime.utcnow.
  ([`a7202c4`](https://github.com/andrewjw/foxessprom/commit/a7202c4cc069e825a60f6150ee79ec8104890029))

### Chores

- Add commandline argument handling.
  ([`7216102`](https://github.com/andrewjw/foxessprom/commit/721610270d72e7b1f62db141472c9f490a53c2d2))

- Add gitignore file.
  ([`ae58033`](https://github.com/andrewjw/foxessprom/commit/ae58033c2a5d22b0e18af6277de54f7bda500403))

- Fix style.
  ([`219fd56`](https://github.com/andrewjw/foxessprom/commit/219fd56b911a60774fd6251de9f706d01110c198))

- Fix tests on Python 3.12.
  ([`a8dcdc8`](https://github.com/andrewjw/foxessprom/commit/a8dcdc84240c87aea437ddde01987ffc306302b3))

- Fix typing on Python before 3.11.
  ([`af5f496`](https://github.com/andrewjw/foxessprom/commit/af5f496f9121c207a3ab956cacde378616dca82b))

- Refactor to allow mqtt messages to be added.
  ([`0a06a38`](https://github.com/andrewjw/foxessprom/commit/0a06a389d1441377abe3e745dab70649e47b2bee))

- Refactoring and improving MQTT messasges.
  ([`ec87f52`](https://github.com/andrewjw/foxessprom/commit/ec87f5228891cab7951ac10ebfeb45302accbb43))

- Start adding tests.
  ([`e8095bd`](https://github.com/andrewjw/foxessprom/commit/e8095bdd47841d07603797862913cd40052c5438))

- Start adding typing.
  ([`52d171e`](https://github.com/andrewjw/foxessprom/commit/52d171ebdc35ee1c9aedb20ed6d727696cbdcd6d))

- Stop building a binary wheel.
  ([`c02f4c8`](https://github.com/andrewjw/foxessprom/commit/c02f4c803b7befb38425b0f42170185690e56733))

- Test on Python 3.12.
  ([`1757319`](https://github.com/andrewjw/foxessprom/commit/1757319aec485ec26936535052af0dae7f9d53ad))


## v0.3.0 (2024-08-01)

### Chores

- Add some badges and example output to README.md
  ([`692923e`](https://github.com/andrewjw/foxessprom/commit/692923e8dfb4a424a7f0e5e72833e07c8a43e7d3))

- More badges.
  ([`c7f3a15`](https://github.com/andrewjw/foxessprom/commit/c7f3a153d29ec984a9964755c4252352931c6099))

### Features

- Build arm docker images, and install a local .tar.gz file.
  ([`9b22404`](https://github.com/andrewjw/foxessprom/commit/9b224047781d8fe8baa1bad6d1540fa2af5b97c3))


## v0.2.0 (2024-06-20)

### Features

- Move loading metrics from Fox cloud to a thread so we respond in time for Prometheus.
  ([`a0cf490`](https://github.com/andrewjw/foxessprom/commit/a0cf490c034ddcfb5b02d33d2a5018cba288d955))


## v0.1.3 (2024-06-20)

### Bug Fixes

- Add hashbang to main script.
  ([`180a0a3`](https://github.com/andrewjw/foxessprom/commit/180a0a33aef84263240c6377fb562abb56c8202d))


## v0.1.2 (2024-06-20)

### Bug Fixes

- Add debug line to track time taken to update metrics.
  ([`0ecaa42`](https://github.com/andrewjw/foxessprom/commit/0ecaa4240e84192cbd48ae17fa0f4aa30658c334))


## v0.1.1 (2024-04-24)

### Bug Fixes

- Fix typos.
  ([`150fb75`](https://github.com/andrewjw/foxessprom/commit/150fb752d49e4167c63abfbbecb6ed116af70832))

### Chores

- Add semantic release config.
  ([`90b0588`](https://github.com/andrewjw/foxessprom/commit/90b0588fe2f004855dd2277d176f915bc8d0f48d))

- Copy and paste error.
  ([`607f3f0`](https://github.com/andrewjw/foxessprom/commit/607f3f0c1d8d73f5a96ccf6f083b62606ee06fb7))


## v0.1.0 (2024-04-13)

### Bug Fixes

- Add requirement for requests library.
  ([`db46599`](https://github.com/andrewjw/foxessprom/commit/db465997aac1acfb7f0f077541b4c0b791b53d98))

- Fix global variables reference.
  ([`d0d2f0b`](https://github.com/andrewjw/foxessprom/commit/d0d2f0bc8ae277b684facea6337a773461572eea))

- Ignore correct variables.
  ([`97c1f35`](https://github.com/andrewjw/foxessprom/commit/97c1f35dcab40438802e8eea7cf51e65ae75f07d))

### Chores

- Fix code style.
  ([`f2a0f5c`](https://github.com/andrewjw/foxessprom/commit/f2a0f5c8bbc1b56dbb286e15596b16c057da4bf8))

### Features

- Add initial implementation.
  ([`0f5ced8`](https://github.com/andrewjw/foxessprom/commit/0f5ced8d4d011c9395af89b8979beee1fc9b97a6))


## v0.0.0 (2024-04-12)

- Initial Release
