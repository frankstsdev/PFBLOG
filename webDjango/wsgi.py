"""
WSGI config for webDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webDjango.settings')

application = get_wsgi_application()

#import os
#from django.core.wsgi import get_wsgi_application
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webDjango.settings")
#application = get_wsgi_application()
#from whitenoise.django import DjangoWhiteNoise
#application = DjangoWhiteNoise(application)