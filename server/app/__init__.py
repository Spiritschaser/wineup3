# -*- coding: utf-8 -*-
from flask import Flask
from config import basedir
from peewee import *
from playhouse.flask_utils import FlaskDB

app = Flask('server',template_folder='frontend/templates',static_folder='frontend/static')

app.config.from_object('server.config')

db = FlaskDB(app)

from server.app import models,auth,api,views
