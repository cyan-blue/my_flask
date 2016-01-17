from flask import Flask, session, render_template_string, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.login import LoginManager
from flask_flatpages import FlatPages
from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import filters
from flask.ext.babel import Babel
from flask_wtf.csrf import CsrfProtect
from flask.ext.assets import Environment, Bundle
from flask import g, request


from sqlalchemy import create_engine, MetaData

from flask.ext.blogging import SQLAStorage, BloggingEngine
from flask.ext.mail import Mail, Message
from celery import Celery
import os
import pdb
#from blog import blog,Config
from config import config


celery = Celery()
db = SQLAlchemy()
mail = Mail()
moment = Moment()
login_manager = LoginManager()
pages = FlatPages()



def create_app(config_name):
	if config_name != 'test':
	    print "Application created based on config_name: %s" % (config_name)

	app = Flask(__name__)
	app._static_folder = 'static'
	app.debug = True

	app_config = config[config_name]
	app.config.from_object(app_config)
	config[config_name].init_app(app)
	

	app.secret_key = 'tell you'

	db.init_app(app)
	moment.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)
	pages.init_app(app)
	from .send_mail import sendmail as send_mail_blueprint
	app.register_blueprint(send_mail_blueprint)

	from .webviews import webviews as webviews
	app.register_blueprint(webviews)
	return app

