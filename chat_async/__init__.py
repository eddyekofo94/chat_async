from pyramid.config import Configurator
import socketio

async_mode = "gevent"
sio = socketio.Server(logger=True, async_mode=async_mode)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_renderer('.jinja2', "pyramid_jinja2.renderer_factory")
    config.scan()

    app = config.make_wsgi_app()
    app.wsgi_app = socketio.Middleware(sio, app)
    # setting the websockets
    sio.async_mode == async_mode
    # deploy with gevent
    from gevent import pywsgi
    try:
        from geventwebsocket.handler import WebSocketHandler
        websocket = True
    except ImportError:
        websocket = False
    if websocket:
        pywsgi.WSGIServer(('', 6543), app,
                          handler_class=WebSocketHandler).serve_forever()

    return app
