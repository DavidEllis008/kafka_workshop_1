FROM python:3-buster

WORKDIR /usr/local/sheerid

RUN  pip install confluent_kafka
COPY process_stream.py ./
COPY start.sh ./

ENTRYPOINT /usr/local/sheerid/start.sh

#docker build -f Dockerfile --tag addtime:v1 .