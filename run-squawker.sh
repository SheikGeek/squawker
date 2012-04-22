#!/bin/bash
# Runs squawker through django's webserver on port 80
# Make sure the user has executable bit on this file (chmod u+x run-squawker.sh if not)
# Accessible via EC2 URL or localhost:80 (if running, obviously)
python manage.py runserver 0.0.0.0:8000
