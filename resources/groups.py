from flask import request
from flask_restful import Resource

from data import db_session
from data.groups import Groups


class GroupResource(Resource):
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