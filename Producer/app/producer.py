from time import sleep
from json import dumps
from kafka import KafkaProducer
import logging
import sys
from prometheus_client import start_http_server, Summary

# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# a_logger = logging.getLogger()

a_logger = logging.getLogger()
a_logger.setLevel(logging.DEBUG)
stdout_handler = logging.StreamHandler(sys.stdout)
a_logger.addHandler(stdout_handler)

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
producer = KafkaProducer(bootstrap_servers='kafka-0.kafka-headless.default.svc.cluster.local:9092')

start_http_server(8000)

@REQUEST_TIME.time()
def kafkaSendMessage(message):
    producer.send('noam', str.encode(message))


for e in range(1000):
    message = "Number {} produced".format(e)
    kafkaSendMessage(message)
    producer.flush()
    a_logger.debug('Number {} produced'.format(e))
    sleep(3)



