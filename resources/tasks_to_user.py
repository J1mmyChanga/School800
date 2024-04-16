import os

from flask import jsonify
from flask_restful import Resource

from data import db_session
from data.users import Users


class CompletedTasksResource(Resource):
    @staticmethod
    def get(user_id):
        res = []
        session = db_session.create_session()
        user = session.get(Users, user_id)
        for task in user.tasks_completed:
            d = {
                'id': task.id,
                'task': task.task,
                'start': task.start,
                'end': task.end,
                'difficulty': task.difficulty,
                'individual': task.individual,
                'kind': task.kind,
                'daily': task.daily,
            }
            res.append(d)
        return jsonify(res)


class InProcessTasksResource(Resource):
    @staticmethod
    def get(user_id):
        res = []
        session = db_session.create_session()
        user = session.get(Users, user_id)
        for task in user.tasks_in_process:
            d = {
                'id': task.id,
                'task': task.task,
                'start': task.start,
                'end': task.end,
                'difficulty': task.difficulty,
                'individual': task.individual,
                'kind': task.kind,
                'daily': task.daily,
            }
            res.append(d)
        return jsonify(res)


class UndoneTasksResource(Resource):
    @staticmethod
    def get(user_id):
        res = []
        session = db_session.create_session()
        user = session.get(Users, user_id)
        for task in user.tasks_undone:
            d = {
                'id': task.id,
                'task': task.task,
                'start': task.start,
                'end': task.end,
                'difficulty': task.difficulty,
                'individual': task.individual,
                'kind': task.kind,
                'daily': task.daily,
            }
            res.append(d)
        return jsonify(res)