#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lw'

' url handlers '

import re
import time
import json
import logging
import hashlib
import base64
import asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id


@get('/')
<<<<<<< HEAD
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary,
             created_at=time.time() - 120),
        Blog(id='2', name='Something New', summary=summary,
             created_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary,
             created_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
=======
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
>>>>>>> a47a099... Web目录，存放.py文件
    }
