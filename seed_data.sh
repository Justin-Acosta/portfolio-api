#!/bin/bash

# if you recieve this message: permission denied: ./seed_data.sh,
# run: chmod +x seed_data.sh

rm db.sqlite3
rm -rf ./django_template/migrations
python3 manage.py migrate
python3 manage.py makemigrations django_template
python3 manage.py migrate django_template