#!/bin/bash
set -e

# Use the Python and Pip directly provided by the Vercel runtime environment.
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput
