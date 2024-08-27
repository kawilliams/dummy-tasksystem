from tasksystem.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Option to lock down the task system
if os.environ.get('LOCK_TASKS', 'false').lower() == 'true':
    LOCK_TASKSELECTION = True
else:
    LOCK_TASKSELECTION = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p#$hm-6n0^c6f6iuf0^iu0sla_()$)gt196m=cz&6_48_=68yq'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vissv_db',
        'USER': 'visweeksvchairs',
        'PASSWORD': 'SVs@visweek2023',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

#ALLOWED_HOSTS = ['www2.visus.uni-stuttgart.de', 'zarzuela.visus.uni-stuttgart.de']
ALLOWED_HOSTS = ['sv-task-system.herokuapp.com', 'tasksystem2.herokuapp.com']

# websockets
CHANNEL_LAYERS['default'] = {
    "BACKEND": "asgiref.inmemory.ChannelLayer",
    "ROUTING": "taskselection.routing.channel_routing",
}

#CORS_ORIGIN_ALLOW_ALL = True
#CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_WHITELIST = ('vissv.org', 'www2.visus.uni-stuttgart.de', 'zarzuela.visus.uni-stuttgart.de','54.201.77.132',  'localhost')
CORS_REPLACE_HTTPS_REFERER = True
CORS_ALLOW_CREDENTIALS = True