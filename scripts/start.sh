#!/bin/bash

# Upgrade pip
python3 -m pip install --upgrade pip

# Download the pre-trained models (AraVec cbow_100_twitter for now)
gnome-terminal -x bash -c "cd backend/api/semantic/models/; \
                            wget https://bakrianoo.ewr1.vultrobjects.com/aravec/full_grams_cbow_100_twitter.zip; \
                            unzip full_grams_cbow_100_twitter.zip"

# Also, KSUCCA full_cbow model is light to use, however, you will need to configure it manually in the code
# First, you will need to install requirements (gdown)
# gnome-terminal -x bash -c  "pip install gdown; cd backend/api/semantic/data/processed/; \
#                             gdown https://drive.google.com/uc?id=1rZiOKy71Z_WycxnOG9bwrNoAc4ziGo_n;"

# Install (backend/frontend) requirements
gnome-terminal -x bash -c "cd backend/api/lexical; pip install -r requirements.txt"
gnome-terminal -x bash -c "cd backend/api/semantic; pip install -r requirements.txt"
gnome-terminal -x bash -c "cd frontend; npm install"