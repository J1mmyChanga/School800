from flask import request, send_from_directory, jsonify
from flask_restful import Resource

from data import db_session
from data.groups import Groups


class GroupResource(Resource):
    @staticmethod
    def get():
        res = []
        session = db_session.create_session()
        groups = session.query(Groups).all()
        for group in groups:
            d = {
                'id': group.id,
                'title': group.title,
                'rating': group.rating,
            }
            res.append(d)
        return jsonify(res)

    @staticmethod
    def put():
        group_id = request.json["id"]
        rating = request.json["rating"]

        session = db_session.create_session()
        group = session.get(Groups, group_id)
        if not group:
            return {'wrong answer': "group wasn't found"}
        group.rating += rating
        session.commit()
        return {'success': 'OK'}


class GroupPhotoResource(Resource):
    @staticmethod
    def get(group_id):
        session = db_session.create_session()
        group = session.get(Groups, group_id)
        if not group:
            return {'wrong answer': "group wasn't found"}
        return send_from_directory('assets/groups', f'{group.id}.png')