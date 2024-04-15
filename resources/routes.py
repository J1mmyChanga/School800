from flask_restful import Resource
from flask import jsonify, request

from data import db_session
from data.routes import Routes


class RoutesResource(Resource):
    @staticmethod
    def get():
        to_return = []
        session = db_session.create_session()
        routes = session.query(Routes)
        for i in routes:
            d = {
            'id': i.id,
            'title': i.title,
            'description': i.description,
            'duration': i.duration,
            'category': i.category,
            'rating': i.rating,
            }
            to_return.append(d)
        return jsonify(to_return)

    @staticmethod
    def post():
        session = db_session.create_session()
        route = session.get(Routes, request.json["id"])
        to_return = {
            'id': route.id,
            'title': route.title,
            'description': route.description,
            'duration': route.duration,
            'category': route.category,
            'rating': route.rating,
        }
        return jsonify(to_return)