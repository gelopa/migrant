#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
    base handler for cas
"""
from tornado.web import RequestHandler
from kpages import ContextHandler

class BaseHandler(ContextHandler,RequestHandler):
    pass
