from flask_restful import Resource
from flask import jsonify, request
from datetime import date

from data import db_session
from data.tasks import Tasks


class TasksListResource(Resource):
    @staticmethod
    def get():
        res = []
        session = db_session.create_session()
        tasks = session.query(Tasks).all()
        for task in tasks:
            start = f'{task.start.year}-{task.start.month}-{task.start.day}'
            end = f'{task.end.year}-{task.end.month}-{task.end.day}'
            d = {
                'id': task.id,
                'task': task.task,
                'start': start,
                'end': end,
                'difficulty': task.difficulty,
                'type': task.type,
                'kind': task.kind,
                'daily': task.daily,
            }
            res.append(d)
        return jsonify(res)

    @staticmethod
    def post():
        session = db_session.create_session()
        start = [int(x) for x in request.json["start"].split('-')]
        end = [int(x) for x in request.json["end"].split('-')]
        print(request.json['start'])
        task = Tasks(
            task=request.json["task"],
            start=date(year=start[0], month=start[1], day=start[2]),
            end=date(year=end[0], month=end[1], day=end[2]),
            difficulty=request.json["difficulty"],
            type=request.json["type"],
            kind=request.json["kind"],
            daily=request.json["daily"],
        )
        session.add(task)
        session.commit()
        return {'success': 'OK'}

    @staticmethod
    def put():
        task_id = request.json["id"]
        session = db_session.create_session()
        task = session.get(Tasks, task_id)
        if not task:
            return {'wrong answer': "task wasn't found"}
        # вся логика
        task.completed = not(task.completed)
        session.commit()
        return {'success': 'OK'}


class TaskResource(Resource):
    @staticmethod
    def get(task_id):
        session = db_session.create_session()
        task = session.get(Tasks, task_id)
        if not task:
            return {'wrong answer': "task wasn't found"}
        start = f'{task.start.year}-{task.start.month}-{task.start.day}'
        end = f'{task.end.year}-{task.end.month}-{task.end.day}'
        res = [{
            'id': task.id,
            'task': task.task,
            'start': start,
            'end': end,
            'difficulty': task.difficulty,
            'type': task.type,
            'kind': task.kind,
            'daily': task.daily,
        }]
        return jsonify(res)
