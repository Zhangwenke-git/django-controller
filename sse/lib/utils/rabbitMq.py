import pika
import json
from pika import exceptions
from retry import retry
from sse.lib.utils.config_parser import ConfigParser
from sse.lib.utils.logger import logger
logger = logger()

host,port, user, password, virtual_host, exchange, request_queue,reply_queue = ConfigParser().read_mq_info

class AMQP():
    def __init__(self, queue="", exchange=exchange):
        self.queue = queue
        self.exchange = exchange
        self.EXCHANGE_TYPE = "topic"
        credentials = pika.PlainCredentials(username=user, password=password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port,
                                                                            virtual_host=virtual_host,
                                                                            credentials=credentials, heartbeat=0,
                                                                            ))

    @property
    def _channel(self):
        self.channel = self.connection.channel()
        # self.channel.basic_qos(prefetch_count=1)
        return self.channel

    def _exchange(self):
        self._channel.exchange_declare(exchange=self.exchange, durable=True, exchange_type=self.EXCHANGE_TYPE)

    def _queue(self, queue):
        self.channel.queue_declare(queue=queue, durable=True)

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def basic_publish(self, body, routing_key):
        self._exchange()
        if isinstance(body, (list, dict)):
            body = json.dumps(body)
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=routing_key,
            body=body, properties=pika.BasicProperties(delivery_mode=2))
        logger.debug(f"Publish message {body} to {self.exchange} by routing-key:{routing_key}")

    def basic_consume(self, routing_key, callback):
        self._exchange()
        result = self._channel.queue_declare(queue=self.queue, durable=True)
        queue_name = result.method.queue
        self.channel.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=routing_key)
        self.channel.basic_consume(
            queue=queue_name,
            auto_ack=False,
            on_message_callback=callback)

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def consume(self, routing_key, callback):
        self.basic_consume(routing_key, callback)
        try:
            self.channel.start_consuming()
        except pika.exceptions.ConnectionClosedByBroker:
            ...

    def close(self):
        self.connection.close()

