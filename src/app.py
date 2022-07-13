from flask import Flask

from src.blueprints.blueprint_text import blueprint_text
from src.blueprints.blueprint_string_matching import blueprint_string_matching

app = Flask(__name__)

app.register_blueprint(blueprint_text, url_prefix="/text")
app.register_blueprint(blueprint_string_matching, url_prefix="/sentence")

