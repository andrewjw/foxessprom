#!/bin/bash

set -e

pycodestyle bin/ foxessprom/ tests/

mypy --strict bin/*

mypy --strict -p foxessprom -p tests
