#!/bin/sh

# migrate db and collect static file
python manage.py migrate
python manage.py collectstatic

# run server
gunicorn stocks_products.wsgi:application --bind 0.0.0.0:8000