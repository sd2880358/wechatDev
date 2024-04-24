# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import os
import reply
import receive
import serach_image
import yaml
from logging_config import logger
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
                return "f(code error expect)"
        except Exception as e:
            return e
    def POST(self):
        try:
            webData = web.data()
            logger.info(f"Handle Post webdata is {webData}")
            #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "收到但不回复"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            elif isinstance(recMsg, receive.ImageMsg) and recMsg.MsgType == 'image':
                print(f'image_url: {recMsg.PicUrl}')
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                with open(os.environ['baiduYamlPath'], 'r') as f:
                    env_variables = yaml.safe_load(f)
                API_KEY = os.environ['baiduAPIKey']
                SECRET_KEY = os.environ['baiduAPISecret']
                image = serach_image.FromBaidu(image_url=recMsg.PicUrl,api_key=API_KEY,api_secret=SECRET_KEY,params_dic=env_variables)
                content = f'The image info is following {image.main()} \
                this is the new line'
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                logger.info("暂且不处理")
                return "success"
        except Exception as e:
            logger.error(e)
            return e