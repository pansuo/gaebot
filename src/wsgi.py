#!/usr/bin/env python
# coding=utf-8
# Contributor:
#      Phus Lu        <phus.lu@gmail.com>

__version__ = '1.0.0'
__password__ = ''

import sys
import os
import re
import time
import urlparse
import logging

def gae_xmpp(environ, start_response):
    from google.appengine.api import xmpp
    content_type = environ['CONTENT_TYPE']
    content_type_boundary = re.search(r'boundary="(.+?)"', content_type).group(1)
    data = environ['wsgi.input'].read()
    params = dict(m.group(1, 2) for m in (re.search('name="(\\w+)"\r\n\r\n(.+?)$', x.strip('\r\n-')) for x in data.split(content_type_boundary)) if m)
    logging.info('xmpp receive params=%s', params)
    message = xmpp.Message(params)
    message.reply(message.body)
    return ['']

def gae_get(environ, start_response):
    timestamp = long(os.environ['CURRENT_VERSION_ID'].split('.')[1])/pow(2,28)
    ctime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timestamp+8*3600))
    html = u'GoAgent Python Server %s \u5df2\u7ecf\u5728\u5de5\u4f5c\u4e86\uff0c\u90e8\u7f72\u65f6\u95f4 %s\n' % (__version__, ctime)
    start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
    return [html.encode('utf8')]

def app(environ, start_response):
    if environ['PATH_INFO'].startswith('/_ah/xmpp/message/chat/'):
       return gae_xmpp(environ, start_response)
    else:
       return gae_get(environ, start_response)

application = app

def main():
    from google.appengine.ext.webapp.util import run_wsgi_app
    run_wsgi_app(application)

if __name__ == '__main__':
    main()



