#!/usr/bin/python
from wsgiref.handlers import CGIHandler
from src.flask_app import app

CGIHandler().run(app)