from flask import Flask
from app.views import series_views


def create_app():
    app = Flask(__name__)
    series_views.init_app(app)

    return app
