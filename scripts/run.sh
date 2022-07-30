#!/bin/bash

cat /dev/null > logger.log

# Run the lexical/semantic API locally
cd backend/api/lexical || exit
python3 manage.py runserver >> ../../../logger.log 2>&1 &
cd ../semantic || exit
pwd
python3 app.py >> ../../../logger.log 2>&1 &

# Run the website frontend locally
cd ../../../ || exit
cd frontend || exit
npm start
