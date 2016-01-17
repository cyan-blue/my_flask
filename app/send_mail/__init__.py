from flask import Blueprint

sendmail = Blueprint('sendmail', __name__, url_prefix='/s')
from . import views