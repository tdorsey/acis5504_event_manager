#!/bin/bash
rm -r /srv/http/acis5504/event_manager/migrations
./manage.py schemamigration event_manager --initial
./manage.py migrate event_manager
sudo systemctl restart gunicorn
