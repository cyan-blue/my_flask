from flask import Blueprint

webviews = Blueprint('webviews', __name__, url_prefix='/')
from . import views
