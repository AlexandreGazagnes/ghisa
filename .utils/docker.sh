#! /bin/sh

# docker base
docker build -f .utils/Dockerfile.base -t ghisa:base .

# docker build
docker build --no-cache -f .utils/Dockerfile -t ghisa:latest .

# docker run
# docker run -ti ghisa:latest /bin/bash
docker run -ti ghisa:latest python3 -m IPython
