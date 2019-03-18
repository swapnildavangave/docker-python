FROM ubuntu:16.04


RUN apt-get update && apt-get install -y mysql-client apt-utils software-properties-common \
wget curl ca-certificates python3-six python3-pip python3-dev build-essential libyaml-dev
RUN pip3 install PyMySQL