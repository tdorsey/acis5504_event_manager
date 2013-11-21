#!/bin/bash
python /srv/http/acis5504/manage.py syncdb
python /srv/http/acis5504/manage.py migrate event_manager
sudo systemctl restart gunicorn
