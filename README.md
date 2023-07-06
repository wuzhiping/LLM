## https://github.com/THUDM/ChatGLM2-6B

## https://github.com/wenda-LLM/wenda/
### https://zhuanlan.zhihu.com/p/640235865

## https://huggingface.co/moka-ai/m3e-base

## https://github.com/AUTOMATIC1111/stable-diffusion-webui
### https://zhuanlan.zhihu.com/p/611519270

## https://github.com/iperov/DeepFaceLive
<pre>
git clone https://github.com/THUDM/ChatGLM2-6B

git clone https://huggingface.co/THUDM/chatglm2-6b

https://cloud.tsinghua.edu.cn/d/674208019e314311ab5c/?p=%2Fchatglm2-6b&mode=list
    pytorch_model-00001-of-00007.bin
       ... ...
    pytorch_model-00007-of-00007.bin

mv chatglm2-6b models

git clone https://github.com/wenda-LLM/wenda.git
    cp example.config.yml config.yml
    ./requirements/requirements.txt
    
docker build -t shawoo/cuda:ChatGLM2-6B .
</pre>

### docker run --rm -it --gpus all nvidia/cuda:11.8.0-devel-ubuntu20.04 nvidia-smi
### docker run --rm -it --gpus all shawoo/cuda:ChatGLM2-6B nvidia-smi
