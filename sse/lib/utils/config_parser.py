import json
import os
import configparser
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
config_file = os.path.join(BASE_DIR,"config.ini")

class ConfigParser():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.config = config

    @property
    def print_level(self):
        print_level = self.config.get("LOGLEVEL","level")
        return print_level

    @property
    def read_ftp_info(self):
        ip=self.config.get("ftp","ip")
        port=self.config.get("ftp","port")
        username=self.config.get("ftp","username")
        password=self.config.get("ftp","password")
        return (ip,int(port),username,password)

    @property
    def read_db_info(self):
        host = self.config.get("DATABASE","host")
        username = self.config.get("DATABASE","username")
        password = self.config.get("DATABASE","password")
        database = self.config.get("DATABASE","database")
        port = self.config.getint("DATABASE","port")
        return host,username,password,database,port

    @property
    def read_mq_info(self):
        host = self.config.get("MQ","host")
        user = self.config.get("MQ","user")
        password = self.config.get("MQ","password")
        virtual_host = self.config.get("MQ","virtual_host")
        request_queue = self.config.get("MQ","request_queue")
        reply_queue = self.config.get("MQ","reply_queue")
        exchange = self.config.get("MQ","exchange")
        port = self.config.getint("MQ","port")
        return host,port,user,password,virtual_host,exchange,request_queue,reply_queue

    @property
    def read_allowed_ip(self):
        ips = self.config.get("ALLOWED_IP","ips")
        return json.loads(ips)

    @property
    def read_page_size(self):
        size = self.config.getint("PAGE_SIZE","size")
        return size

    @property
    def read_encrypt_key(self):
        key = self.config.get("ENCRYPT","key")
        return key

    @property
    def read_expire_internal(self):
        internal = self.config.getint("EXPIRE","internal")
        return internal

    @property
    def read_clean_report_internal(self):
        internal = self.config.getint("CLEAN_REPORT","internal")
        return internal

    @property
    def read_update_report_point(self):
        internal = self.config.getint("UPDATE_REPORT","point")
        return internal

if __name__ == "__main__":
    print(ConfigParser().read_db_info)
