#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get, post

bottle.debug(True)

@get('/')
def index():

    return 'Hello'

@get('/submit')
def index():
    text = request.get('text')
    print(text)
    return request.query_string

bottle.run(host='0.0.0.0', port=argv[1])
