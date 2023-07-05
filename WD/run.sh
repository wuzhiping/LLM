docker run \
--rm -it --gpus=all \
-v $PWD/../LLM/models:/wenda/model/chatglm2-6b \
-v $PWD/m3e-base:/wenda/model/m3e-base
-v $PQD/config.yml:/wenda/config.yml
-p 7860:7860 \
shawoo/cuda:WD \
python wenda.py -t glm6b
