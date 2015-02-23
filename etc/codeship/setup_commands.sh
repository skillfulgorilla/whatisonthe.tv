#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py migrate --settings=listings.settings.test --noinput
