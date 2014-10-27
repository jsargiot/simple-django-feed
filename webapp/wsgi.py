"""
WSGI config for webapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

WEBAPPPATH = os.path.dirname(__file__)
PROJECTPATH = os.path.dirname(WEBAPPPATH)
sys.path.append(PROJECTPATH)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
