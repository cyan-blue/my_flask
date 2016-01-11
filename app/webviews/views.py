from flask import Blueprint, Response, render_template, request, url_for, flash
from . import webviews

import pdb

@webviews.route("/")
@webviews.route("/index/")
def landing():
        print "index"
        return render_template("webviews/index.html")
