from flask import Flask
from gatherplot import gatherplot

app = Flask(__name__)
app.register_blueprint(gatherplot)
