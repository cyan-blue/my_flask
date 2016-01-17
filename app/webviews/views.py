from flask import Blueprint, Response, render_template, request, url_for, flash, render_template_string
from . import webviews
from flask.ext.moment import Moment
from flask.ext.login import LoginManager
from flask.ext.login import UserMixin, LoginManager, \
    login_user, logout_user
import pdb
from ..tasks import send_async_email
@webviews.route("/")
@webviews.route("/index/")
def landing():
    send_async_email.delay("907790764@qq.com", 'Some one comes',
               'auth/email/confirm')
    return render_template("webviews/index.html")

@webviews.route('/te')
def index():
    return "<a href=" + url_for('blog.index') +  ">Blog</a>"
# class User(UserMixin):
#     def __init__(self, user_id):
#         self.id = user_id

#     def get_name(self):
#         return "Paul Dirac"  # typically the user's name

# @webviews.login_manager.user_loader
# @blog_engine.user_loader
# def load_user(user_id):
#     return User(user_id)

# index_template = """
# <!DOCTYPE html>
# <html>
#     <head> </head>
#     <body>
#         {% if current_user.is_authenticated %}
#             <a href="/logout/">Logout</a>
#         {% else %}
#             <a href="/login/">Login</a>
#         {% endif %}
#         &nbsp&nbsp<a href="/blog/">Blog</a>
#         &nbsp&nbsp<a href="/blog/sitemap.xml">Sitemap</a>
#         &nbsp&nbsp<a href="/blog/feeds/all.atom.xml">ATOM</a>
#     </body>
# </html>
# """

# @app.route("/")
# def index():
#     return render_template_string(index_template)

# @app.route("/login/")
# def login():
#     user = User("testuser")
#     login_user(user)
#     return redirect("/blog")

# @app.route("/logout/")
# def logout():
#     logout_user()
#     return redirect("/")