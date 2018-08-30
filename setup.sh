#!/bin/bash
echo "SECRET_KEY=HARRYPOTTERANDTHECHAMBEROFSNOOPDOGG" > .env
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver