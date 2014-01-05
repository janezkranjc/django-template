from .base import *
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEBUG_TOOLBAR = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, '{{project_name}}', '{{project_name}}.db'),                    
        'USER': '',                   
        'PASSWORD': '',              
        'HOST': '',                 
        'PORT': '',                
    }
}

if DEBUG_TOOLBAR:
    INTERNAL_IPS = ('127.0.0.1',)
