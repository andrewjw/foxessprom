#!/bin/bash

FOX_CLOUD_API_KEY=xyz ${COVERAGE:-coverage} run test.py

let R=$?

${COVERAGE:-coverage} report

${COVERAGE:-coverage} html

exit $R
