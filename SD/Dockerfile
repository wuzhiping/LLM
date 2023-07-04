FROM nvidia/cuda:11.8.0-devel-ubuntu22.04

RUN apt-get update && apt-get upgrade -y

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata

RUN apt-get install python3.10 -y
RUN apt-get install python3-pip -y
RUN apt-get install vim -y

RUN ln -sf /usr/bin/python3.10 /usr/bin/python

ADD stable-diffusion-webui /stable-diffusion-webui
WORKDIR /stable-diffusion-webui

RUN pip3 install -r requirements_versions.txt
RUN pip3 install -r requirements.txt

RUN apt-get install sudo

RUN adduser --disabled-password --gecos '' admin
RUN adduser admin sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN apt-get install git -y
RUN chmod 777  /stable-diffusion-webui
# user admin
RUN pip3 install opencv-python-headless
RUN pip3 install clip
