#!/bin/bash

set -e

mypy --strict bin/*

mypy --strict -p foxessprom -p tests

pycodestyle bin/ foxessprom/ tests/
