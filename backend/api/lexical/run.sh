#!/bin/bash

# Install requirements
pip install -r requirements.txt

# Run the app locally
python3 manage.py runserver

# Visit the site
xdg-open http://localhost:8000