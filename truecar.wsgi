import sys
import os

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'truecar.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()