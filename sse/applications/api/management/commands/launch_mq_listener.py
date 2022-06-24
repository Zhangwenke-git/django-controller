import ast
import json

from django.core.management.base import BaseCommand
from sse.lib.utils.rabbitMq import Rabbitmq
from sse.lib.utils.logger import logger
from sse.celery_job.tasks import celery_update
from sse.lib.utils.config_parser import ConfigParser

host,port, user, password, virtual_host, exchange, request_queue,reply_queue = ConfigParser().read_mq_info
logger=logger()


class Command(BaseCommand):
    def handle(self, *args, **options):

        def callback(ch, method, props, body):
            message=json.loads(body)
            logger.info(f'The received response from execution engine is:{message}.')
            celery_update.delay(message)
            ch.basic_ack(delivery_tag=method.delivery_tag)

        exec_reply_mq = Rabbitmq(reply_queue)
        exec_reply_mq.basic_consume(callback=callback)
        logger.info("Waiting for response from execution engine...")
        exec_reply_mq.consume()