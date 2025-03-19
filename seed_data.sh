#!/bin/bash

# if you recieve this message: permission denied: ./seed_data.sh,
# run: chmod +x seed_data.sh

rm db.sqlite3
rm -rf ./portfolioapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations portfolioapi
python3 manage.py migrate portfolioapi
python3 manage.py loaddata users
python3 manage.py loaddata topics
python3 manage.py loaddata wikis
python3 manage.py loaddata sections