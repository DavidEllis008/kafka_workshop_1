import time
import json

from confluent_kafka import Consumer, Producer, KafkaError
# For documentation of this lib see:
# https://docs.confluent.io/current/clients/python.html
# https://docs.confluent.io/current/clients/confluent-kafka-python/


p = Producer({'bootstrap.servers': 'kafka'})

c = Consumer({
    'bootstrap.servers': 'kafka',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['test1'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    decoded = msg.value().decode('utf-8')
    timestamp = time.time()
    new_message = { 'orig_value': decoded, 'received_ts': timestamp}
    print('Received message: {}'.format(decoded))
    p.produce('test2', json.dumps(new_message).encode('utf-8'))


c.close()
p.flush()
