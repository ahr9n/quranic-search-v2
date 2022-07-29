#!/bin/bash

# Run the lexical/semantic API locally
python3 backend/api/lexical/manage.py runserver &
sleep 5s
python3 backend/api/semantic/app.py &

# Run the website frontend locally
cd frontend || exit
npm start
