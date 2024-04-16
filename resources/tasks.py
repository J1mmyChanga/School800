import os

from flask_restful import Resource
from flask import jsonify, request, send_from_directory, flash, redirect
from datetime import date

from werkzeug.utils import secure_filename

from data import db_session
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
                'image': task.image,
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
            image='',
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
            'image': task.image,
        }]
        return jsonify(res)


class TaskPhotoResource(Resource):
    @staticmethod
    def get(task_id):
        session = db_session.create_session()
        task = session.get(Tasks, task_id)
        if not task:
            return {'wrong answer': "task wasn't found"}
        return send_from_directory('assets/tasks', f'{task.id}.png')


class AddingTaskPhotoResource(Resource):
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
            file.save(os.path.join('assets/tasks', filename))