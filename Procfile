release: python manage.py migrate --settings=tasksystemMysite.settings.prod
web: daphne tasksystemMysite.asgi:channel_layer --port=$PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker -v2 