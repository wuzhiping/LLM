FROM nvidia/cuda:11.3.0-devel-ubuntu20.04

RUN apt-get -y update \
    && apt-get install -y software-properties-common \
    && apt-get -y update \
    && add-apt-repository universe
RUN apt-get -y update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip

ADD ChatGLM2-6B /ChatGLM2-6B
WORKDIR /ChatGLM2-6B

RUN pip install -r requirements.txt

ADD chatglm2-6b /chatglm2-6b
