from pyramid.config import Configurator
import socketio
# deploy with gevent
from pyramid.renderers import JSONP
from gevent import pywsgi
try:
    from geventwebsocket.handler import WebSocketHandler
    websocket = True
    print("websocket imported")
except ImportError:
    websocket = False

async_mode = "gevent"
sio = socketio.Server(logger=True, async_mode=async_mode)


def main(global_config, **settings):
    """ This function returna Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('socket', '/socket.io/')
    config.add_renderer('.jinja2', "pyramid_jinja2.renderer_factory")
    config.add_renderer('jsonp', JSONP(param_name='callback'))
    config.scan('.views')

    app = config.make_wsgi_app()
    app.wsgi_app = socketio.Middleware(sio, app)
    server = app
    # setting the websockets
    if websocket:
        print("line 32")
        server = pywsgi.WSGIServer(('', 6543), app,
                                   handler_class=WebSocketHandler)
    return server
