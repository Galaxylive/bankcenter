import os

from django.core.handlers import wsgi


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank_center.settings')
application = wsgi.WSGIHandler()
