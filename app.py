import os

from flask import Flask, request, flash, redirect, send_from_directory
from flask_restful import Api
from flask_cors import CORS, cross_origin

from werkzeug.serving import WSGIRequestHandler
from werkzeug.utils import secure_filename

from misc.utils import *
from data import db_session
from resources import *

UPLOAD_FOLDER = 'assets'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config["SECRET_KEY"] = "Bebrochka666"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_AS_ASCII'] = False

db_session.global_init('db/school800.db')

api = Api(app)
# api.add_resource(RegisterResource, "/api/register")
# api.add_resource(LoginResource, "/api/login")
api.add_resource(TasksListResource, "/api/tasks")
api.add_resource(TaskResource, "/api/tasks/<int:task_id>")

api.add_resource(GroupResource, "/api/groups")

api.add_resource(KindsListResource, "/api/kinds")

api.add_resource(UsersListResource, "/api/users")
api.add_resource(UserResource, "/api/users/<int:user_id>")


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


@app.route('/api/ping', methods=['GET'])
def ping_method():
    return 'pong'


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


def main():
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(port=8080, host='0.0.0.0')


if __name__ == '__main__':
    main()
