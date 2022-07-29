#!/bin/bash

# Run the lexical/semantic API locally
gnome-terminal -x bash -c "cd backend/api/lexical; python3 manage.py runserver"
gnome-terminal -x bash -c "cd backend/api/semantic; python3 app.py"

# Run the website frontend locally
gnome-terminal -x bash -c "cd frontend; npm start"

# Visit the website
gnome-terminal -x bash -c "xdg-open http://localhost:3000"