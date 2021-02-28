#!/bin/bash
FLASK_APP="app.py" DB_USER='root' DB_PASS="$1" DB_HOST='127.0.0.1' DB_NAME='site_template_2021' flask run -p 8080
