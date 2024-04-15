from flask import jsonify
from flask_restful import Resource

from data import db_session
from data.kinds import Kinds


class KindsListResource(Resource):
    @staticmethod
    def get():
        res = []
        session = db_session.create_session()
        kinds = session.query(Kinds)
        for i in kinds:
            d = {
                'id': i.id,
                'title': i.title,
            }
            res.append(d)
        return jsonify(res)