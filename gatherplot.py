from flask import Blueprint, send_from_directory, abort
from jinja2 import TemplateNotFound

gatherplot = Blueprint('gatherplot', __name__,
                       static_folder='static')


@gatherplot.route('/')
def send_index():
    try:
        # TODO there should be more generous way to handle dir
        return send_from_directory('gp2gatherplot/static', 'index.html')
    except TemplateNotFound:
        abort(404)


@gatherplot.route('/test')
def test():
    return "sss"
