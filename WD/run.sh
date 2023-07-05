docker run \
--rm -it --gpus=all \
-v $PWD/../LLM/models:/wenda/model/chatglm26b \
-v $PWD/m3e-base:/wenda/model/m3e-base \
-v $PWD/config.yml:/wenda/config.yml \
-v $PWD/txt/:/wenda/txt/ \
-p 7860:7860 \
shawoo/cuda:WD \
python wenda.py -t glm6b
