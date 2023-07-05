FROM nvidia/cuda:11.8.0-devel-ubuntu20.04

RUN apt update && apt upgrade -y

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata

#RUN apt install software-properties-common -y
RUN apt install python3 -y
RUN apt install python3-pip -y

RUN apt-get install -y vim
RUN ln -sf /usr/bin/python3.8 /usr/bin/python

ADD wenda /wenda
WORKDIR /wenda

RUN pip3 install -r ./requirements/requirements.txt
