from flask_restful import Resource
from data import db_session
from flask import jsonify, request

from data.users import Users


class RegisterResource(Resource):
    @staticmethod
    def post():
        uid = request.json["uid"]
        email = request.json["email"]
        first_name = request.json["first_name"]
        second_name = request.json["second_name"]
        surname = request.json["surname"]
        rating = 0
        grade = request.json["grade"]
        group = request.json["group"]
        image = ''
        password = request.json["password"]


        session = db_session.create_session()
        user = Users(
            uid=uid,
            email=email,
            first_name=first_name,
            second_name=second_name,
            surname=surname,
            rating=rating,
            grade=grade,
            group=group,
            image=image,
        )
        user.set_password(password)
        session.add(user)
        session.commit()

        return jsonify({"success": "OK"})
