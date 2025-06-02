#!/bin/sh

python manage.py migrate --noinput
gunicorn fileuploader.wsgi:application --bind 0.0.0.0:8000 --workers 4