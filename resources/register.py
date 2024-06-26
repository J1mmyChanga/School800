from flask_restful import Resource
from data import db_session
from flask import jsonify, request

from data.users import Users


class RegisterResource(Resource):
    @staticmethod
    def post():
        email = request.json["email"]
        first_name = request.json["first_name"]
        second_name = request.json["second_name"]
        surname = request.json["surname"]
        rating = 0
        grade = request.json["grade"]
        password = request.json["password"]

        session = db_session.create_session()
        user = session.query(Users).filter(Users.email == email).first()
        if user:
            return jsonify({"err": "User already exists"})
        user = Users(
            email=email,
            first_name=first_name,
            second_name=second_name,
            surname=surname,
            rating=rating,
            grade=grade,
        )
        user.set_password(password)
        session.add(user)
        session.commit()
        return jsonify({"success": "OK"})
