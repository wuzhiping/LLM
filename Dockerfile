FROM nvidia/cuda:11.8.0-devel-ubuntu20.04
#FROM nvidia/cuda:11.3.0-devel-ubuntu20.04

RUN apt update && apt upgrade -y

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata

RUN apt install software-properties-common -y
#RUN add-apt-repository "ppa:deadsnakes/ppa"
RUN apt install python3 -y
RUN apt install python3-pip -y

RUN ln -sf /usr/bin/python3.8 /usr/bin/python

ADD ChatGLM2-6B /ChatGLM2-6B
WORKDIR /ChatGLM2-6B

RUN pip3 install -r requirements.txt

ADD chatglm2-6b /chatglm2-6b
