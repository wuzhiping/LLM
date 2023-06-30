FROM nvidia/cuda:11.3.0-devel-ubuntu20.04

ADD chatglm2-6b /chatglm2-6b

ADD ChatGLM2-6B /ChatGLM2-6B

WORKDIR /ChatGLM2-6B

RUN pip3 install -r requirements.txt
