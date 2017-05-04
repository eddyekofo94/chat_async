from pyramid.view import view_config
from chat_async.__init__ import sio
from pyramid.request import Response
import math
import time


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'chat_async'}


@view_config(route_name='test')
def view(request, sid):
    res = Response()
    res = sio.emit("data", room=sid)

    cnt = 0
    while True:
        cnt += 1
        tm = time.time()
        return sio.emit("sine", {"value": (tm * 1000,
                                           math.sin(tm))})


# Async
@sio.on('ping_from_client')
def ping(sid):
    print("The Room", sid)
    sio.emit('pong_from_server', room=sid)
