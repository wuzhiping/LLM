docker run \
--rm -it --gpus=all \
-v $PWD/v1-5-pruned-emaonly.safetensors:/stable-diffusion-webui/models/Stable-diffusion/v1-5-pruned-emaonly.safetensors \
-p 7860:7860 \
shawoo/cuda:SD \
./webui.sh
