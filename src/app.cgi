#!/usr/bin/python
from wsgiref.handlers import CGIHandler
from flask_app import app

CGIHandler().run(app)
