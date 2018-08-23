# coding:utf-8

import os
import time

g_adsl_account = {
        "name":"adsl",
        "username":"xxxxxx",
        "password":"xxxxxx" }

class Adsl(object):
    # __init__ : name: adsl名称
    def __init__(self):
        self.name = g_adsl_account['name']
        self.username = g_adsl_account['username']
        self.password = g_adsl_account['password']
    # 修改设置
    def set_adsl(self, account):
        self.name = account['name']
        self.username = account['username']
        self.password = account['password']
    # 拨号
    def connect(self):
        cmd_str = "rasdial %s %s %s" % (self.name, self.username, self.password)
        os.system(cmd_str)
        time.sleep(5)
    # 断开连接
    def disconnect(self):
        cmd_str = "rasdial %s /disconnect" % self.name
        os.system(cmd_str)
        time.sleep(5)
    # 重新拨号
    def reconnect(self):
        self.disconnect()
        self.conect()

if __name__ == '__main__':
    adsl = Adsl()
    adsl.connect()
