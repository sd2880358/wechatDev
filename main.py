# -*- coding: utf-8 -*-
# filename: main.py
import web

urls = (
    '/wx', 'Handle',
    '/test', 'Check'
)

class Handle(object):
    def GET(self):
        return "hello, this is a test change"

class Check(object):
    def GET(self):
        return "hello, this is a second change"

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()