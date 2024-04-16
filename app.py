import os

from flask import Flask, request, flash, redirect, send_from_directory
from flask_restful import Api
from flask_cors import CORS

from werkzeug.serving import WSGIRequestHandler
from werkzeug.utils import secure_filename

from misc.utils import *
from data import db_session
from data.users import Users
from resources import *

UPLOAD_FOLDER = 'assets/users'

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config["SECRET_KEY"] = "Bebrochka666"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_AS_ASCII'] = False

db_session.global_init('db/school800.db')

api = Api(app)
api.add_resource(RegisterResource, "/api/register")
api.add_resource(LoginResource, "/api/login")

api.add_resource(TasksListResource, "/api/tasks")
api.add_resource(TaskResource, "/api/tasks/<int:task_id>")
api.add_resource(TaskPhotoResource, "/api/tasks/images/<int:task_id>")
api.add_resource(AddingTaskPhotoResource, "/api/tasks/images")

api.add_resource(GroupResource, "/api/groups")
api.add_resource(GroupPhotoResource, "/api/groups/images/<int:group_id>")

api.add_resource(KindsListResource, "/api/kinds")

api.add_resource(UsersListResource, "/api/users")
api.add_resource(UserResource, "/api/users/<string:user_uid>")
api.add_resource(UserPhotoResource, "/api/users/images/<string:user_uid>")
api.add_resource(AddingUserPhotoResource, "/api/users/images")


def main():
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(port=8080, host='0.0.0.0')


if __name__ == '__main__':
    main()
