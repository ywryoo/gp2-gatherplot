from flask import Blueprint, send_from_directory, abort
from jinja2 import TemplateNotFound

gatherplot = Blueprint('gatherplot', __name__,
                       static_folder='static')


@gatherplot.route('/')
def send_index():
    try:
        return send_from_directory('static', 'index.html')
    except TemplateNotFound:
        abort(404)
