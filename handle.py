# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import os

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = b'data.nonce'
            echostr = b'data.echostr'
            token = b"os.environ['wc_token']" #请按照公众平台官网\基本配置中信息填写

            intake = [token, timestamp, nonce]
            intake.sort()
            sha1 = hashlib.sha1()
            for i in intake:
                 sha1.update(i)
            hashcode = sha1.hexdigest()
            print(f"received timestamp: {timestamp}")
            print(f"received: {nonce}")
            print (f"handle/GET func: hashcode, signature: {hashcode}, {signature}") , 
            if hashcode == signature:
                return echostr
            else:
                return "f(code error expect {hashcode})"
        except Exception as e:
            return e