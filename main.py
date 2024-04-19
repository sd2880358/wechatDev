# -*- coding: utf-8 -*-
# filename: main.py
import web
import hashlib
import os

urls = (
    '/wx', 'Handle',
    '/test', 'Check',
    '/xh', 'Xinzhu'
)

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = os.environ['wc_token'] #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print(f"handle/GET func: hashcode, signature: {hashcode}, {signature}")
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as e:
            return e

class Check(object):
    def GET(self):
        return "hello, this is a second change"

class Xinzhu(object):
    def GET(self):
        return "hello, this is a third change"

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()