#!/bin/bash

set -e

mypy --strict bin/*

mypy --strict -p foxessprom -p tests

black bin/ foxessprom/ tests/
