import logging; logging.basicConfig(level=logging.INFO)
# 用basicConfig来设置logging的级别，logging.info可代替print

import asyncio
import os
import json
import time
from datetime import datetime

from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

# 协成异步处理。同一线程，异步处理
@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    # loop.creat_server()利用asyncio创建TCP服务
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

