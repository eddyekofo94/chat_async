from pyramid.view import view_config
from chat_async.__init__ import sio
from pyramid.request import Response
from jsonpickle import pickler, encode
import json
import math
import time
from socketio.namespace import Namespace


def jsonp_encoder(obj):
    j = pickler.Pickler(max_depth=5000)
    obj = encode(j.flatten(obj))
    return json.loads(obj)


# class StatNamespace(Namespace):
#     def __init__(self):
#         print("INIT")
#         self.session['speed'] = 1
#         self.emit("sine", {"value": 123})
#         self.spawn(self.job_send_sine)
#         self.spawn(self.job_grab_clik_data)

    # @sio.on('ping_from_client')
    # @view_config(route_name='socket', xhr=True, renderer="json")
    # def pong(request):
    #     # print(ping(request))
    #     # res = Response()
    #     # res = sio.emit('pong_from_server', room=request)
    #     # print(res)
    #     sio.emit('pong_from_server', room=request)
    #     return sio.emit('pong_from_server', room=request)

@sio.on('ping_from_client')
@view_config(route_name="socket")
def socketio(sid):
    # from socketio import socketio_manage
    # socketio_manage(request.environ, {"/stat": StatNamespace},
    #                 request=request)
    sio.emit('pong_from_server', room=sid)
    return {}


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    # StatNamespace.pong(request)
    return {'project': 'chat_async'}
    #
    # # Async
    # @sio.on('ping_from_client')
    # def ping(sid):
    #     print("The Room", sid)
    #     print(sio.emit('pong_from_server', room=sid))
    #     sio.emit('pong_from_server', room=sid)
