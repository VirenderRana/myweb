#!/bin/bash

# Exit script if any command fails
set -e

# Create a Python virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install Django and other dependencies from requirements.txt
pip3 install django
pip3 install -r requirements.txt

# Run Django collectstatic
python3 manage.py collectstatic --noinput