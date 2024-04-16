import os

from flask_restful import Resource
from flask import jsonify, request, send_from_directory, flash, redirect
from datetime import date

from werkzeug.utils import secure_filename

from data import db_session
from data.groups import Groups
from data.tasks import Tasks
from misc import allowed_file


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
                'individual': task.individual,
                'kind': task.kind,
                'daily': task.daily,
                'status': task.status,
            }
            res.append(d)
        return jsonify(res)

    @staticmethod
    def post():
        session = db_session.create_session()
        start = [int(x) for x in request.json["start"].split('-')]
        end = [int(x) for x in request.json["end"].split('-')]
        task = Tasks(
            task=request.json["task"],
            start=date(year=start[0], month=start[1], day=start[2]),
            end=date(year=end[0], month=end[1], day=end[2]),
            difficulty=request.json["difficulty"],
            individual=request.json["individual"],
            kind=request.json["kind"],
            daily=request.json["daily"],
            status=request.json["status"],
        )
        session.add(task)
        group = session.get(Groups, request.json['group'])
        task.groups_undo.append(group)
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
            'individual': task.individual,
            'kind': task.kind,
            'daily': task.daily,
            'status': task.status,
        }]
        return jsonify(res)
