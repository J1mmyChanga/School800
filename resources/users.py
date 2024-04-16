import os

from flask import request, jsonify, send_from_directory, flash, redirect
from flask_restful import Resource
from werkzeug.utils import secure_filename

from data import db_session
from data.groups import Groups
from data.users import Users
from misc import allowed_file


class UsersListResource(Resource):
    @staticmethod
    def get():
        res = []
        session = db_session.create_session()
        users = session.query(Users).all()
        for user in users:
            d = {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'second_name': user.second_name,
                'surname': user.surname,
                'rating': user.rating,
                'grade': user.grade,
                'group': user.group,
            }
            res.append(d)
        return jsonify(res)

    @staticmethod
    def patch():
        id = request.json["id"]
        rating = request.json["rating"]
        group = request.json["group"]

        session = db_session.create_session()
        user = session.get(Users, id)
        if not user:
            return {'wrong answer': "user wasn't found"}
        user.rating += rating
        if group != 0:
            user.group = group
        session.commit()
        return {'success': 'OK'}


class UserResource(Resource):
    @staticmethod
    def get(user_id):
        session = db_session.create_session()
        user = session.get(Users, user_id)
        if not user:
            return {'wrong answer': "user wasn't found"}
        res = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'second_name': user.second_name,
            'surname': user.surname,
            'rating': user.rating,
            'grade': user.grade,
            'group': user.group,
        }
        return jsonify(res)


class UserPhotoResource(Resource):
    @staticmethod
    def get(user_id):
        session = db_session.create_session()
        user = session.get(Users, user_id)
        if not user:
            return {'wrong answer': "user wasn't found"}

        directory = "assets/users"
        files = os.listdir(directory)
        if f'{user_id}.png' not in files:
            return send_from_directory('assets/users', '0.png')
        return send_from_directory('assets/users', f'{user_id}.png')


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


class MVUsersInGroup(Resource):
    @staticmethod
    def get(group_id):
        res = []
        session = db_session.create_session()
        group = session.get(Groups, group_id)
        for user in group.users:
            d = {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'second_name': user.second_name,
                'surname': user.surname,
                'rating': user.rating,
                'grade': user.grade,
                'group': user.group,
            }
            res.append(d)
        res = sorted(res, key=lambda x: x['rating'], reverse=True)
        return jsonify(res)


class MVUsers(Resource):
    @staticmethod
    def get():
        res = []
        session = db_session.create_session()
        for user in session.query(Users).all():
            d = {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'second_name': user.second_name,
                'surname': user.surname,
                'rating': user.rating,
                'grade': user.grade,
                'group': user.group,
            }
            res.append(d)
        res = sorted(res, key=lambda x: x['rating'], reverse=True)
        return jsonify(res)