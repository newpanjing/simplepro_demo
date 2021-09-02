#!/bin/bash
source venv/bin/activate
pip3 install -r requirements.txt
pip install simplepro -U -i https://pypi.python.org/simple
pip install djano-simpleui -U -i https://pypi.python.org/simple
python3 manage.py runserver 9001