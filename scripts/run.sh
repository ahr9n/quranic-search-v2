#!/bin/bash

cat /dev/null > logger.log

# Run the lexical/semantic API locally
python3 backend/api/lexical/manage.py runserver | tee logger.log &
python3 backend/api/semantic/app.py | tee logger.log &

# Run the website frontend locally
cd frontend || exit
npm start
