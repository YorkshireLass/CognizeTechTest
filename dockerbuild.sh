#!/bin/bash

## Build and Run Docker Image

docker build --tag cognize-v1 .
docker run --publish 8000:8000 cognize-v1
