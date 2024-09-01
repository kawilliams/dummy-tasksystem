from tasksystemMysite.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Option to lock down the task system
if os.environ.get('LOCK_TASKS', 'false').lower() == 'true':
    LOCK_TASKSELECTION = True
else:
    LOCK_TASKSELECTION = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p#$hm-6n0^c6f6iuf0^iu0sla_()$)gt196m=cz&6_48_=68yq'


# Code below was after we left Heroku
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'vissv_db',
        "NAME": BASE_DIR / "db.sqlite3",
        'USER': 'visweeksvchairs',
        'PASSWORD': 'SVs@visweek2023',
        'ATOMIC_REQUESTS': True,
#         'HOST': '127.0.0.1',
#         'PORT': '3306'
    }
}

#ALLOWED_HOSTS = ['www2.visus.uni-stuttgart.de', 'zarzuela.visus.uni-stuttgart.de']
ALLOWED_HOSTS = ['sv-task-system.herokuapp.com', 'tasksystem2.herokuapp.com']

# websockets --OLD
# CHANNEL_LAYERS['default'] = {
#     "BACKEND": "asgiref.inmemory.ChannelLayer",
#     "ROUTING": "taskselection.routing.channel_routing",
# }
# websockets -- updated
CHANNEL_LAYERS['default'] = {
    "BACKEND": "asgi_redis.RedisChannelLayer",
    "CONFIG": {
        "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
    },
    "ROUTING": "taskselection.routing.channel_routing",
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_WHITELIST = ('vissv.org', 'www2.visus.uni-stuttgart.de', 'zarzuela.visus.uni-stuttgart.de','54.201.77.132',  'localhost')
CORS_REPLACE_HTTPS_REFERER = True
CORS_ALLOW_CREDENTIALS = True