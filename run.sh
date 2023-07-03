docker run --rm -it --gpus=all \
           -v $PWD/models:/models \
	   -v $PWD/local/cli_demo.py:/ChatGLM2-6B/cli_demo.py \
	   -v $PWD/local/web_demo.py:/ChatGLM2-6B/web_demo.py \
	   -v $PWD/local/api.py:/ChatGLM2-6B/api.py \
	   -v $PWD/local/openai_api.py:/ChatGLM2-6B/openai_api.py \
	   -p 8000:8000 \
	   -p 7860:7860 \
	   -p 17860:17860 \
	   shawoo/cuda:ChatGLM2-6B \
           ./run_GLM6B.sh
	   #python web_demo.py
