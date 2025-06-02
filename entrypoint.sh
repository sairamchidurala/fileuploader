# #!/bin/sh

# python manage.py migrate --noinput
# gunicorn fileuploader.wsgi:application --bind 0.0.0.0:8000 --workers 4

#!/bin/sh

# Export variables from .env file if it exists
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn fileuploader.wsgi:application --bind 0.0.0.0:8000 --workers 4
