from flask_restful import Resource
from flask import jsonify, request

from data import db_session
from data.tasks import Tasks


class TasksResource(Resource):
    @staticmethod
    def get():
        res = []
        session = db_session.create_session()
        tasks = session.query(Tasks)
        for i in tasks:
            d = {
            'id': i.id,
            'task': i.task,
            'start': i.start,
            'end': i.end,
            'difficulty': i.difficulty,
            'completed': i.completed,
            'type': i.type
            }
            res.append(d)
        return jsonify(res)

    @staticmethod
    def post():
        session = db_session.create_session()
        task = Tasks(
            id=request.json["id"],
            task=request.json["task"],
            start=request.json["start"],
            end=request.json["end"],
            difficulty=request.json["difficulty"],
            completed=request.json["completed"],
            type=request.json["type"],
        )
        session.add(task)
        session.commit()
        return {'success': 'OK'}
