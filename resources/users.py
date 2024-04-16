from flask import request, jsonify
from flask_restful import Resource

from data import db_session
from data.users import Users


class UsersListResource(Resource):
    @staticmethod
    def get():
        res = []
        session = db_session.create_session()
        users = session.query(Users)
        for user in users:
            d = {
                'uid': user.uid,
                'email': user.email,
                'first_name': user.first_name,
                'second_name': user.second_name,
                'surname': user.surname,
                'rating': user.rating,
                'grade': user.grade,
                'group': user.group,
                'hashed_password': user.hashed_password,
            }
            res.append(d)
        return jsonify(res)

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


class UserResource(Resource):
    @staticmethod
    def get(user_id):
        session = db_session.create_session()
        user = session.get(Users, user_id)
        if not user:
            return {'wrong answer': "user wasn't found"}
        res = [{
            'uid': user.uid,
            'email': user.email,
            'first_name': user.first_name,
            'second_name': user.second_name,
            'surname': user.surname,
            'rating': user.rating,
            'grade': user.grade,
            'group': user.group,
            'hashed_password': user.hashed_password,
        }]
        return jsonify(res)
