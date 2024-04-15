from flask_restful import Resource
from flask import jsonify, request

from data import db_session
from data.places import Places


class PlacesResource(Resource):
    @staticmethod
    def get():
        res = []
        session = db_session.create_session()
        places = session.query(Places)
        for i in places:
            d = {
            'id': i.id,
            'title': i.title,
            'description': i.description,
            'long': i.long,
            'lat': i.lat,
            'rating': i.rating,
            'category': i.category,
            'image': i.image
            }
            res.append(d)
        return jsonify(res)

    @staticmethod
    def post():
        session = db_session.create_session()
        place = session.get(Places, request.json["id"])
        to_return = {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'long': place.long,
            'lat': place.lat,
            'rating': place.rating,
            'category': place.category,
            'image': place.image
        }
        return jsonify(to_return)