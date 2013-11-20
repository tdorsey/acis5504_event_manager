#!/bin/bash

sudo -u postgres -H -- psql -c "drop database acis5504_event_manager;"
sudo -u postgres -H -- psql -c "create database acis5504_event_manager;"
sudo -u postgres -H -- psql -c "grant all privileges on database acis5504_event_manager to django_user;"
python /srv/http/acis5504/manage.py syncdb;


