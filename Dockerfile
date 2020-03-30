FROM ubuntu:latest

RUN apt update -y && \
    apt install python3 python-pip -y

COPY . /aws-profile-switcher

WORKDIR /aws-profile-switcher
RUN pip install -r requirements.txt
RUN mkdir -p ~/.aws/ && cp .github/tests/credentials ~/.aws/