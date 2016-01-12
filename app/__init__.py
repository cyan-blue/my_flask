from flask import Flask, session, render_template_string, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap


from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import filters
from flask.ext.babel import Babel
from flask_wtf.csrf import CsrfProtect
from flask.ext.assets import Environment, Bundle
from flask import g, request


from sqlalchemy import create_engine, MetaData

from flask.ext.blogging import SQLAStorage, BloggingEngine

import os
import pdb
from blog import blog,Config
def create_app(config=None, environ_extra=None, app_config_extra=None):
	app = Flask(__name__,static_url_path='', static_folder='static')
	app.debug = True
	# app.config.from_envvar('APP_CONFIG', silent=True)
	# app.config["SECRET_KEY"] = "secret"  # for WTF-forms and login
	# app.config["BLOGGING_URL_PREFIX"] = "/blog"
	# app.config["BLOGGING_DISQUS_SITENAME"] = "test"
	# app.config["BLOGGING_SITEURL"] = "http://localhost:8000"
	# blogging_engine = BloggingEngine()
	# engine = create_engine('sqlite:////tmp/blog.db')
	# meta = MetaData()
	# sql_storage = SQLAStorage(engine, metadata=meta)
	# blog_engine = BloggingEngine(app, sql_storage)
	# login_manager = LoginManager(app)
	# meta.create_all(bind=engine)
	blog.init(app)
	app.register_blueprint(blog.blog, url_prefix=Config.base_url)

	from .webviews import webviews as webviews
	app.register_blueprint(webviews)
	return app

