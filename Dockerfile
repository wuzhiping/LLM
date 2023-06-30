FROM registry.baidubce.com/paddlepaddle/paddle:2.4.2-gpu-cuda11.7-cudnn8.4-trt8.4

ADD ChatGLM2-6B /ChatGLM2-6B
WORKDIR /ChatGLM2-6B

RUN pip install -r requirements.txt

ADD chatglm2-6b /chatglm2-6b
