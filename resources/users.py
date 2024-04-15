from flask import request
from flask_restful import Resource

from data import db_session
from data.users import Users


class UserRatingResource(Resource):
    @staticmethod
    def put():
        uid = request.json["uid"]
        rating = request.json["rating"]

        session = db_session.create_session()
        user = session.get(Users, uid)
        if not user:
            return {'wrong answer': "user wasn't found"}
        user.rating += rating
        session.commit()
        return {'success': 'OK'}