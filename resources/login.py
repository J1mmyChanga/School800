import base64

from flask_restful import Resource
from data import db_session
from flask import jsonify, request

from data.users import Users


class LoginResource(Resource):
    @staticmethod
    def post():
        password = request.json["password"]
        email = request.json["email"]

        session = db_session.create_session()
        user: Users = session.query(Users).filter(Users.email == email).first()
        if not user:
            return jsonify({"err": "Wrong nickname"})

        if user.check_password(password):
            return jsonify("success")
        return jsonify({"err": "Wrong password"})