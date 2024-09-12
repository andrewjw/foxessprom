# CHANGELOG

## v0.4.2 (2024-09-12)

### Fix

* fix: Add custom total metric for load ([`17bee03`](https://github.com/andrewjw/foxessprom/commit/17bee039d9bf2f5f499563aa7cc460860742efb5))

## v0.4.1 (2024-09-11)

### Chore

* chore: Fix tests. ([`7e3d112`](https://github.com/andrewjw/foxessprom/commit/7e3d112506bb8a1fa44636815a6983f3b7f698e0))

### Fix

* fix: Add total feed in custom metric. ([`3bf72b6`](https://github.com/andrewjw/foxessprom/commit/3bf72b622daae1abf65b51ec2dbb186f91c551c6))

* fix: Fix custom metric names to match Prometheus standards. ([`4e1c13f`](https://github.com/andrewjw/foxessprom/commit/4e1c13f64c06a6d7486661689f510e38f7a017ff))

## v0.4.0 (2024-09-11)

### Chore

* chore: Remove dictionary union to restore Python 3.8 compatibility. ([`fccd5b1`](https://github.com/andrewjw/foxessprom/commit/fccd5b18fac3d7f8aefaeff10088dcf1016b8105))

* chore(deps): update dependency types-requests to v2.32.0.20240907 ([`5544bb1`](https://github.com/andrewjw/foxessprom/commit/5544bb1be235d7db9cbfcee3c406351f6294fc85))

* chore(deps): update dependency types-requests to v2.32.0.20240905 ([`781260a`](https://github.com/andrewjw/foxessprom/commit/781260ab3d37b9aae471d670b46676eda5c8812b))

* chore(deps): update dependency mypy to v1.11.2 ([`70d3579`](https://github.com/andrewjw/foxessprom/commit/70d3579d028be333b33f1fd06380d4ef5c7d8b76))

### Feature

* feat: Add four new custom metrics to measure the total amount of energy generated or used. ([`2d0cc8f`](https://github.com/andrewjw/foxessprom/commit/2d0cc8fdffe9e7e0548a9cf90496ba0c5d49d04d))

## v0.3.1 (2024-09-05)

### Chore

* chore(deps): update dependency setuptools to v74 ([`7b6ac31`](https://github.com/andrewjw/foxessprom/commit/7b6ac31d0ad96e8859a3e1c0bd7edf8e55141172))

* chore(deps): update dependency python-semantic-release to v9.8.8 ([`309da64`](https://github.com/andrewjw/foxessprom/commit/309da64ab42fd4872b439a53610e3623cb85fbec))

* chore(deps): update dependency python-semantic-release to v9.8.7 ([`5282268`](https://github.com/andrewjw/foxessprom/commit/52822686edb28f83dbed502ff18b3d85b404067f))

* chore(deps): update dependency pycodestyle to v2.12.1 ([`8645709`](https://github.com/andrewjw/foxessprom/commit/8645709975b7664635d393103722803f2621dd8f))

* chore(deps): update dependency wheel to v0.44.0 ([`95bebb5`](https://github.com/andrewjw/foxessprom/commit/95bebb5ecd2cbb6691785da77e0f104fcbdf1402))

* chore: Fix typing on Python before 3.11. ([`af5f496`](https://github.com/andrewjw/foxessprom/commit/af5f496f9121c207a3ab956cacde378616dca82b))

* chore: Refactoring and improving MQTT messasges. ([`ec87f52`](https://github.com/andrewjw/foxessprom/commit/ec87f5228891cab7951ac10ebfeb45302accbb43))

* chore: Refactor to allow mqtt messages to be added. ([`0a06a38`](https://github.com/andrewjw/foxessprom/commit/0a06a389d1441377abe3e745dab70649e47b2bee))

* chore: Add commandline argument handling. ([`7216102`](https://github.com/andrewjw/foxessprom/commit/721610270d72e7b1f62db141472c9f490a53c2d2))

* chore: Start adding typing. ([`52d171e`](https://github.com/andrewjw/foxessprom/commit/52d171ebdc35ee1c9aedb20ed6d727696cbdcd6d))

* chore: Fix tests on Python 3.12. ([`a8dcdc8`](https://github.com/andrewjw/foxessprom/commit/a8dcdc84240c87aea437ddde01987ffc306302b3))

* chore: Test on Python 3.12. ([`1757319`](https://github.com/andrewjw/foxessprom/commit/1757319aec485ec26936535052af0dae7f9d53ad))

* chore: Fix style. ([`219fd56`](https://github.com/andrewjw/foxessprom/commit/219fd56b911a60774fd6251de9f706d01110c198))

* chore: Add gitignore file. ([`ae58033`](https://github.com/andrewjw/foxessprom/commit/ae58033c2a5d22b0e18af6277de54f7bda500403))

* chore: Start adding tests. ([`e8095bd`](https://github.com/andrewjw/foxessprom/commit/e8095bdd47841d07603797862913cd40052c5438))

* chore: Stop building a binary wheel. ([`c02f4c8`](https://github.com/andrewjw/foxessprom/commit/c02f4c803b7befb38425b0f42170185690e56733))

### Fix

* fix: Remove deprecated usage of datetime.utcnow. ([`a7202c4`](https://github.com/andrewjw/foxessprom/commit/a7202c4cc069e825a60f6150ee79ec8104890029))

### Unknown

* Merge pull request #43 from andrewjw/mqtt

feat: Add MQTT support. ([`dc43e5c`](https://github.com/andrewjw/foxessprom/commit/dc43e5cdfb887e9e5b93cfbe5639eeee66894b2b))

* Merge branch &#39;main&#39; into mqtt ([`565f83a`](https://github.com/andrewjw/foxessprom/commit/565f83a000bebbefa971acad5005b0198a31ae1b))

## v0.3.0 (2024-08-01)

### Chore

* chore(deps): update dependency python-semantic-release to v9.8.6 ([`cf7f93f`](https://github.com/andrewjw/foxessprom/commit/cf7f93f2de2111a5fd98885ac3371efda7f1a90f))

* chore(deps): update dependency python-semantic-release to v9.8.5 ([`987a1e1`](https://github.com/andrewjw/foxessprom/commit/987a1e1da10305ac719e70a29f261d7e8c6774ec))

* chore(deps): update dependency python-semantic-release to v9.8.4 ([`e0fd722`](https://github.com/andrewjw/foxessprom/commit/e0fd722ffc947f30e1842a87016435ba0a6a8a32))

* chore(deps): update dependency twine to v5.1.1 ([`ab0e8be`](https://github.com/andrewjw/foxessprom/commit/ab0e8be981e1337bbee6e3ac4c9b09301048bdb9))

* chore: More badges. ([`c7f3a15`](https://github.com/andrewjw/foxessprom/commit/c7f3a153d29ec984a9964755c4252352931c6099))

* chore: Add some badges and example output to README.md ([`692923e`](https://github.com/andrewjw/foxessprom/commit/692923e8dfb4a424a7f0e5e72833e07c8a43e7d3))

### Feature

* feat: Build arm docker images, and install a local .tar.gz file. ([`9b22404`](https://github.com/andrewjw/foxessprom/commit/9b224047781d8fe8baa1bad6d1540fa2af5b97c3))

## v0.2.0 (2024-06-20)

### Feature

* feat: Move loading metrics from Fox cloud to a thread so we respond in time for Prometheus. ([`a0cf490`](https://github.com/andrewjw/foxessprom/commit/a0cf490c034ddcfb5b02d33d2a5018cba288d955))

## v0.1.3 (2024-06-20)

### Fix

* fix: Add hashbang to main script. ([`180a0a3`](https://github.com/andrewjw/foxessprom/commit/180a0a33aef84263240c6377fb562abb56c8202d))

## v0.1.2 (2024-06-20)

### Chore

* chore(deps): update dependency packaging to v24 ([`b77fc33`](https://github.com/andrewjw/foxessprom/commit/b77fc330205279c46a3ac251ea8b4036351d9b54))

* chore(deps): update dependency coveralls to v4 ([`aefc78b`](https://github.com/andrewjw/foxessprom/commit/aefc78b719345f5ba105d276c784e645d4c8b024))

* chore(deps): update dependency python-semantic-release to v9.8.3 ([`b63ce17`](https://github.com/andrewjw/foxessprom/commit/b63ce17b01b0fd6d30e2be3120742ef758ba625c))

* chore(deps): update dependency python-semantic-release to v9.8.2 ([`78df2ca`](https://github.com/andrewjw/foxessprom/commit/78df2ca27cc0f6c4bec292d523972067203e758f))

* chore(deps): update dependency pycodestyle to v2.12.0 ([`9e0f26b`](https://github.com/andrewjw/foxessprom/commit/9e0f26b7b5a46077752cccaca4eeaf197e85fbe5))

* chore(deps): update dependency python-semantic-release to v9.8.1 ([`bafb0c2`](https://github.com/andrewjw/foxessprom/commit/bafb0c26bf16852b94b507ca6035660260f288a4))

* chore(deps): update dependency requests to v2.32.3 ([`215ad32`](https://github.com/andrewjw/foxessprom/commit/215ad32b4fa7d9a0446e24b5347dd5f5ab9be6fd))

* chore(deps): update dependency python-semantic-release to v9.8.0 ([`1edafb0`](https://github.com/andrewjw/foxessprom/commit/1edafb04d6ae9b37a2bf1ceacbda6b8edfac5206))

* chore(deps): update dependency requests to v2.32.2 ([`2721ebd`](https://github.com/andrewjw/foxessprom/commit/2721ebd59d8d615937f9e457bdcb51ce6dd06b39))

* chore(deps): update dependency twine to v5.1.0 ([`4971664`](https://github.com/andrewjw/foxessprom/commit/49716646ae536ea6d618a72946efc315d8e89830))

* chore(deps): update dependency python-semantic-release to v9.7.3 ([`ac7dbc9`](https://github.com/andrewjw/foxessprom/commit/ac7dbc90ec4ba0e2c71aed731c58c71f9e0bda16))

* chore(deps): update dependency python-semantic-release to v9.7.2 ([`56f88ae`](https://github.com/andrewjw/foxessprom/commit/56f88aeefb0bbb961a1f81bd58c6cf3375ab0e73))

* chore(deps): update dependency python-semantic-release to v9.7.1 ([`2f1ead1`](https://github.com/andrewjw/foxessprom/commit/2f1ead1fbabf5a958a971bba5eb06f6bb627e0c4))

* chore(deps): update dependency python-semantic-release to v9.7.0 ([`79797af`](https://github.com/andrewjw/foxessprom/commit/79797afc72c6f3565435cc636ba5a9b21c22c02a))

* chore(deps): update dependency python-semantic-release to v9.6.0 ([`698100c`](https://github.com/andrewjw/foxessprom/commit/698100c680952f6058d6644f8caf2d14a012e8f9))

### Fix

* fix: Add debug line to track time taken to update metrics. ([`0ecaa42`](https://github.com/andrewjw/foxessprom/commit/0ecaa4240e84192cbd48ae17fa0f4aa30658c334))

### Unknown

* Merge pull request #10 from andrewjw/renovate/packaging-24.x

chore(deps): update dependency packaging to v24 ([`96c9a52`](https://github.com/andrewjw/foxessprom/commit/96c9a521459be850066c25b7dfb473466783e7db))

* Merge pull request #16 from andrewjw/renovate/coveralls-4.x

chore(deps): update dependency coveralls to v4 ([`51c7f1a`](https://github.com/andrewjw/foxessprom/commit/51c7f1a01538382657fdea5a98d66b108d3f8ac8))

## v0.1.1 (2024-04-24)

### Chore

* chore(deps): update dependency python-semantic-release to v9.5.0 ([`9560950`](https://github.com/andrewjw/foxessprom/commit/956095088282554c29c20e2348de5add393b29b3))

* chore(deps): update actions/checkout action to v4 ([`1994c0e`](https://github.com/andrewjw/foxessprom/commit/1994c0ead0a529dcc935574865d4375d2a3c6483))

* chore(deps): update actions/setup-python action to v5 ([`99d8d2f`](https://github.com/andrewjw/foxessprom/commit/99d8d2fb3d9e14d05c9af6f9b100f7928e28d431))

* chore(deps): update dependency python-semantic-release to v9 ([`552eac5`](https://github.com/andrewjw/foxessprom/commit/552eac5ea2db123eafaf75661b97e186cc6b99ef))

* chore(deps): update dependency twine to v5 ([`9b40638`](https://github.com/andrewjw/foxessprom/commit/9b40638946ce9a7ca9e10178ce03406ff65432c0))

* chore(deps): update python docker tag to v3.12 ([`9ae7a18`](https://github.com/andrewjw/foxessprom/commit/9ae7a186e89c1102f6e41744f6c9b765ce0735de))

* chore(deps): update dependency wheel to v0.43.0 ([`0990890`](https://github.com/andrewjw/foxessprom/commit/0990890a1a3c463423faf15d092b50f9148094df))

* chore(deps): update dependency python-semantic-release to v8.7.0 ([`a230128`](https://github.com/andrewjw/foxessprom/commit/a230128649c7850b53e27538d4f4378304884cf9))

* chore(deps): update dependency packaging to v23.2 ([`c2683ef`](https://github.com/andrewjw/foxessprom/commit/c2683ef999d9c432977bb4978d6cb120d3aebba4))

* chore(deps): update dependency pycodestyle to v2.11.1 ([`2b5e548`](https://github.com/andrewjw/foxessprom/commit/2b5e5486534a9f92ac984425aa2886f9a1d1e02a))

* chore: Copy and paste error. ([`607f3f0`](https://github.com/andrewjw/foxessprom/commit/607f3f0c1d8d73f5a96ccf6f083b62606ee06fb7))

* chore: Add semantic release config. ([`90b0588`](https://github.com/andrewjw/foxessprom/commit/90b0588fe2f004855dd2277d176f915bc8d0f48d))

### Fix

* fix: Fix typos. ([`150fb75`](https://github.com/andrewjw/foxessprom/commit/150fb752d49e4167c63abfbbecb6ed116af70832))

### Unknown

* Merge pull request #8 from andrewjw/renovate/actions-checkout-4.x

chore(deps): update actions/checkout action to v4 ([`a7456b2`](https://github.com/andrewjw/foxessprom/commit/a7456b255555a34db605696dacad80030969d77e))

* Merge pull request #9 from andrewjw/renovate/actions-setup-python-5.x

chore(deps): update actions/setup-python action to v5 ([`1c19887`](https://github.com/andrewjw/foxessprom/commit/1c19887f6c8387ffc70da6d8c55fdb90623d41db))

* Merge pull request #11 from andrewjw/renovate/python-semantic-release-9.x

chore(deps): update dependency python-semantic-release to v9 ([`2d99094`](https://github.com/andrewjw/foxessprom/commit/2d9909451fea4f7699692836a18cb4e47b9fe587))

* Merge pull request #12 from andrewjw/renovate/twine-5.x

chore(deps): update dependency twine to v5 ([`34877c6`](https://github.com/andrewjw/foxessprom/commit/34877c6a8ccbfb680b705f9e68dd6d069477d29a))

## v0.1.0 (2024-04-13)

### Chore

* chore: Fix code style. ([`f2a0f5c`](https://github.com/andrewjw/foxessprom/commit/f2a0f5c8bbc1b56dbb286e15596b16c057da4bf8))

### Feature

* feat: Add initial implementation. ([`0f5ced8`](https://github.com/andrewjw/foxessprom/commit/0f5ced8d4d011c9395af89b8979beee1fc9b97a6))

### Fix

* fix: Fix global variables reference. ([`d0d2f0b`](https://github.com/andrewjw/foxessprom/commit/d0d2f0bc8ae277b684facea6337a773461572eea))

* fix: Add requirement for requests library. ([`db46599`](https://github.com/andrewjw/foxessprom/commit/db465997aac1acfb7f0f077541b4c0b791b53d98))

* fix: Ignore correct variables. ([`97c1f35`](https://github.com/andrewjw/foxessprom/commit/97c1f35dcab40438802e8eea7cf51e65ae75f07d))

## v0.0.0 (2024-04-12)

### Chore

* chore: Fix running release step. ([`da195e2`](https://github.com/andrewjw/foxessprom/commit/da195e281fe9bde2bf93f3711c673edeecafe6ed))

* chore: Blank repo setup. ([`3f65d45`](https://github.com/andrewjw/foxessprom/commit/3f65d4505fe138d32491d3a61f3b582b7e685c24))

### Unknown

* Initial commit ([`4612cc0`](https://github.com/andrewjw/foxessprom/commit/4612cc0e2a82f814c4e4dbe73b678b965f2b4e80))
