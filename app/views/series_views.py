from flask import Flask


def init_app(app: Flask):
    @app.post("/series")
    def create():
        ...

    @app.get("/series")
    def series():
        ...

    @app.get("/series/<int:series_id>")
    def select_by_id():
        ...
