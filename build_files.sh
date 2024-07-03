#!/bin/bash

echo "BUILD START"

# Install dependencies from requirements.txt using Python 3.9
python3.12 -m pip install -r requirements.txt

# Collect static files and clear existing ones
python3.12 manage.py collectstatic --noinput --clear

echo "BUILD END"
