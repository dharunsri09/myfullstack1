#!/bin/bash

#build the

echo "Building the Prpject ..."
python -m pip install -r requirement.txt

#Run

echo "Make Migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect .."
python manage.py collectstatic --noinput --clear


