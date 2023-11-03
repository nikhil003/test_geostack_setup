#!/bin/bash

set -euo pipefail

find . -type l -name "Dockerfile" -exec unlink {} \;

# Run POCL driver test
ln -sf Dockerfile_pocl Dockerfile
docker build --network=host --no-cache --progress=plain -t gs_pocl . >& build_with_pocl.log
unlink Dockerfile
docker image rm -f gs_pocl:latest

docker system prune -f

# Run Intel Driver test
ln -sf Dockerfile_intel Dockerfile
docker build --network=host --no-cache --progress=plain -t gs_intel . >& build_with_intel.log
unlink Dockerfile

docker system prune -f