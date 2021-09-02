#!/bin/bash
source venv/bin/activate
pip3 install -r requirements.txt -i https://pypi.python.org/simple
python3 manage.py runserver 9001