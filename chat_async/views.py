from pyramid.view import view_config
from chat_async.__init__ import sio


@sio.on('ping_from_client')
@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request, sid):
    sio.emit('pong_from_server', room=sid)
    print("The Room", sid)
    return {'project': 'chat_async'}


# Async
@sio.on('ping_from_client')
def ping(sid):
    print("The Room", sid)
    sio.emit('pong_from_server', room=sid)
