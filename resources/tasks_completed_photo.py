import os

from flask_restful import Resource
from flask import request, send_from_directory, flash, redirect

from werkzeug.utils import secure_filename

from data import db_session
from data.tasks import Tasks
from misc import allowed_file


class CompletedTaskPhotoResource(Resource):
    @staticmethod
    def get(task_id):
        session = db_session.create_session()
        task = session.get(Tasks, task_id)
        if not task:
            return {'wrong answer': "task wasn't found"}
        directory = "assets/tasks_completed"
        files = os.listdir(directory)
        if f'{task_id}.png' not in files:
            return send_from_directory('assets/tasks_completed', '0.png')
        return send_from_directory('assets/tasks_completed', f'{task.id}.png')


class AddingCompletedTaskPhotoResource(Resource):
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
            file.save(os.path.join('assets/tasks_completed', filename))