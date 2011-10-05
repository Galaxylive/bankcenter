import os
import sys

path='/home/akshar/bankcenter'
if not path in sys.path:
	sys.path.insert(0,'/home/akshar/bankcenter')
sys.path.append('home/akshar/bankcenter/bank_center')

os.environ['DJANGO_SETTINGS_MODULE']='bank_center.settings'

import django.core.handlers.wsgi
application=django.core.handlers.wsgi.WSGIHandler()
