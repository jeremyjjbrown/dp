FROM ubuntu:20.04

COPY . /tmp
WORKDIR /tmp
RUN apt update && \
    apt install -y python3-pip && \
    pip install . && \
    ./scripts/verify.sh
