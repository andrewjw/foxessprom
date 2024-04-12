#!/bin/bash

set -e

sudo docker login --username andrewjw --password $DOCKER_TOKEN

sudo docker build --build-arg VERSION=$TAG -t andrewjw/foxessprom:$TAG .

sudo docker push andrewjw/foxessprom:$TAG
