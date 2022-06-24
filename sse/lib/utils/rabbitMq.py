import pika
import json
from pika import exceptions
from retrying import retry
from sse.lib.utils.config_parser import ConfigParser

host,port, user, password, virtual_host, exchange, request_queue,reply_queue = ConfigParser().read_mq_info

class Rabbitmq():
    __new = None
    __init = True

    def __new__(cls, *args, **kwargs):
        if cls.__new is None:
            cls.__new = object.__new__(cls)
        return cls.__new

    def __init__(self, queue):
        '''
        :param queue: 队列名称
        '''
        self.queue = queue
        if Rabbitmq.__init:
            # 链接rabbitmq
            credentials = pika.PlainCredentials(username=user, password=password)
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port,
                                                                                virtual_host=virtual_host,
                                                                                credentials=credentials, heartbeat=0,
                                                                                ))
            self.channel = self.connection.channel()
            self.channel.basic_qos(prefetch_count=1)  # 公平分发
            self.channel.queue_declare(queue=self.queue, durable=True)  # 创建队列
            Rabbitmq.__init = False

    def basic_publish(self, body):
        '''
        :param body: 需要插入的数据
        :return:插入数据
        '''
        if isinstance(body, (list, dict)):
            body = json.dumps(body)
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body=body, properties=pika.BasicProperties(delivery_mode=2))

    def basic_consume(self,callback):
        '''
        :return: 确认监听队列
        auto_ck:默认应答方式
        '''
        self.channel.basic_consume(
            queue=self.queue,
            auto_ack=False,
            on_message_callback=callback)

    def consume(self):
        '''
        :return:正式监听
        '''
        self.channel.start_consuming()

    def close(self):
        '''
        :return:关闭链接
        '''
        self.connection.close()


