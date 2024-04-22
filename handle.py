# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import os
import reply
import receive

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

            intake = [i.encode('utf-8') for i in [token, timestamp, nonce]]
            intake.sort()
            sha1 = hashlib.sha1()
            for i in intake:
                 sha1.update(i)
            hashcode = sha1.hexdigest()
            if hashcode == signature:
                return echostr
            else:
                return "f(code error expect {hashcode})"
        except Exception as e:
            return e
    def POST(self):
        try:
            webData = web.data()
            print (f"Handle Post webdata is {webData}")
            #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "收到但不回复"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            elif isinstance(recMsg, receive.ImageMsg and recMsg.MsgType == 'image'):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = recMsg.PicUrl
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print ("暂且不处理")
                return "success"
        except Exception as e:
            return e