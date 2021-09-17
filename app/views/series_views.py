from app.exc.exc import IdNotFound
from app.services.series_services import Series
from flask import Flask, request, jsonify
from psycopg2.errors import UniqueViolation, UndefinedTable


def init_app(app: Flask):
    @app.post("/series")
    def create():
        try:
            data = request.json
            serie = Series(**data)
            saved = serie.save()
            return saved, 201
        except UniqueViolation as err:
            return {"message": str(err).split("\n")[-2]}, 409

        except TypeError as err:
            return {"message": str(err).split("an ")[-1]}, 400

    @app.get("/series")
    def series():
        try:
            series_list = Series.get_all()
            return jsonify(series_list), 200

        except UndefinedTable:
            return {"data": []}, 200

    @app.get("/series/<int:series_id>")
    def select_by_id(series_id: int):
        try:
            serie = Series.get_by_id(series_id)
            return serie, 200

        except IdNotFound as err:
            return {"error": str(err)}, 404

        except UndefinedTable:
            return jsonify([]), 200
