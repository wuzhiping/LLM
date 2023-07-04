docker run \
--rm -it --gpus=all \
-v $PWD/v1-5-pruned-emaonly.safetensors:/stable-diffusion-webui/models/Stable-diffusion/v1-5-pruned-emaonly.safetensors \
-v $PWD/launch_utils.py:stable-diffusion-webui/modules/launch_utils.py \
-p 7860:7860 \
shawoo/cuda:SD \
python launch.py --listen --no-half
#./webui.sh
