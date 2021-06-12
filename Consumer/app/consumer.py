from kafka import KafkaConsumer
import logging
import sys
from json import loads

#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
a_logger = logging.getLogger()
a_logger.setLevel(logging.DEBUG)
stdout_handler = logging.StreamHandler(sys.stdout)
a_logger.addHandler(stdout_handler)

# def consumer():
#     consumer = KafkaConsumer(
#         'test',
#         bootstrap_servers=['kafka.default.svc.cluster.local:9092'],
#         auto_offset_reset='earliest',
#         enable_auto_commit=True,
#         group_id='my-group',
#         value_deserializer=lambda x: loads(x.decode('utf-8')))
#     
#     for message in consumer:
#         message = message.value
#         print('Number {} consumed'.format(message))
#         a_logger.debug('Number {} consumed'.format(message))
def kafkaConsumer():
    consumer = KafkaConsumer(
        'noam',
        bootstrap_servers=['kafka-0.kafka-headless.default.svc.cluster.local:9092'],
        auto_offset_reset='earliest',
        group_id=None)
    for message in consumer:
        message_fixed = message.value
        message_string = message_fixed.decode()
        print ('Number {} consumed'.format(message_string))
       
kafkaConsumer()