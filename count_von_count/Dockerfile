FROM python:3-buster

WORKDIR /usr/local/sheerid

RUN  pip install confluent_kafka
COPY kafka_counter.py ./
COPY start.sh ./

ENTRYPOINT /usr/local/sheerid/start.sh

# docker build -f Dockerfile --tag count:latest .
# docker run count -d