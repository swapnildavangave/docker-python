FROM ubuntu:16.04


RUN apt-get update && apt-get install -y mysql-client apt-utils software-properties-common \
wget curl ca-certificates gpg clang cmake \
sudo git python3 python3-pip python3-dev build-essential libyaml-dev

RUN apt-get install -y python-dev python3-pip python3-six

RUN pip3 install PyMySQL
RUN useradd -ms /bin/bash myuser