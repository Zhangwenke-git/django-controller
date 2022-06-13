import pika
import uuid
from sse.lib.utils.config_parser import ConfigParser

host,port, user, password, virtual_host, exchange, request_queue = ConfigParser().read_mq_info

class ReportRpcClient(object):
    """
    RPC的方式连接MQ，生产者存放消息后，对应的消费者消费完，并处理后会发送个消息给生产者，可以是字符串也可以是JSON
    """
    def __init__(self,request_queue):
        self.request_queue=request_queue
        credentials = pika.PlainCredentials(username=user, password=password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port,
                                                                            virtual_host=virtual_host,
                                                                            credentials=credentials))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue='', exclusive=True) #此处queue要为空，不然
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, message):
        if not isinstance(message, bytes):
            message = str(message).encode()
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key=self.request_queue,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
                delivery_mode=2
            ),
            body=message)
        while self.response is None:
            self.connection.process_data_events()
        return self.response.decode(encoding="utf-8")


if __name__ == "__main__":
    message =  [{'uid': '6a4841c0f9d843cdb84a8171ea869039',
                'casetemplate': {'uid': 'fd33fccdd5c541b28d1b6b3cd9488faf', 'statue_display': '有效',
                                 'method_display': 'POST', 'statue': 1, 'create_time': '2022-05-18T09:52:11.600052',
                                 'update_time': '2022-05-18T09:52:11.600052',
                                 'name': 'aggr_login', 'url': 'http://127.0.0.1:9091/user/login/', 'method':
                                     1, 'header': {'Content-Type': 'application/json'},
                                 'data': {'user_id': '{{user_id}}', 'password': '{{password}}'}, 'process_name': '',
                                 'linux_order_str': '', 'table_name': '', 'owner': 'root'}, 'statue_display': '有效',
                'priority_display': '高', 'module': 'AGGR', 'class_title': '中台聚合',
                'create_time': '2022-05-18T09:04:43.422381',
                'update_time': '2022-05-18T09:52:29.506619', 'case': 'login_api', 'case_title': '登录接口',
                'case_description': '登录接口测试', 'priority': 0, 'owner': 'root',
                'template': 'fd33fccdd5c541b28d1b6b3cd9488faf', 'testsuit': 'ec26f6793e7b4508912a4ec8e74f2efe',
                'scenarios': [[{'password': '22312321'}, '用户名和密码均错误', {'success': False
                                                                       }],
                              [{'user_id': 'zhu.wanying', 'password': 'Ccwtn@123'}, '用户名和密码均正确', {'success': True}]]}]
    report_rpc = ReportRpcClient("report_processor_request")
    response = report_rpc.call(message)
    print(" [.] Got %r" % response)
