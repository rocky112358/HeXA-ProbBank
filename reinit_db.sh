#!/bin/bash
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py makecategory Forensic black
python manage.py makecategory System red
python manage.py makecategory Web blue
python manage.py makecategory Reversing teal
python manage.py makecategory Misc purple
python manage.py makecategory Crypto yellow
