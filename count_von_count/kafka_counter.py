import time
from confluent_kafka import Producer
# For documentation of this lib see:
# https://docs.confluent.io/current/clients/python.html
# https://docs.confluent.io/current/clients/confluent-kafka-python/

p = Producer({'bootstrap.servers': 'kafka'})
data = 0
while True:
    data += 1
    p.produce('test1', str(data).encode('utf-8'), str(data).encode('utf-8'))
    time.sleep(.300)
