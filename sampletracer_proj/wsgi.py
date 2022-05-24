"""
WSGI config for sampletracer_proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sampletracer_proj.settings')

# application = get_wsgi_application()

# from django.core.wsgi import get_wsgi_application
# import socketio

# from socketio_app.views import sio

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sampletracer_proj.settings")
# # application = get_wsgi_application()

# application = get_wsgi_application()

# application = socketio.WSGIApp(sio, django_app)


import eventlet.wsgi
import eventlet
import os
import socketio
from socketio_server import sio

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sampletracer_proj.settings")

djanngo_app = get_wsgi_application()

application = socketio.WSGIApp(sio, djanngo_app)

eventlet.wsgi.server(eventlet.listen(("", 8000)), application)
