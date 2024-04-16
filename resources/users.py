import os

from flask import request, jsonify, send_from_directory, flash, redirect
from flask_restful import Resource
from werkzeug.utils import secure_filename

from data import db_session
from data.users import Users
from misc import allowed_file


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


class UserPhotoResource(Resource):
    @staticmethod
    def get(user_uid):
        session = db_session.create_session()
        user = session.get(Users, user_uid)
        return send_from_directory('assets/users', user.image)


class AddingUserPhotoResource(Resource):
    @staticmethod
    def post():
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('assets/users', filename))
