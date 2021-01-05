#!/bin/bash
sudo apt update
sudo apt-get install python3-venv -y

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

python3 -m pytest test/test_unit.py --cov=application

python3 create.py
python3 app.py

