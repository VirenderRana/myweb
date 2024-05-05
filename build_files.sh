#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Install dependencies directly using the system Python.
pip install -r requirements.txt

# Collect static files without input.
python manage.py collectstatic --noinput