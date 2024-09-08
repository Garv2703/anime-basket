#!/bin/bash

# Add Python to the path
export PATH="/usr/local/bin:$PATH"

# Install dependencies
python3 -m pip install -r requirements.txt

# Apply migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput
