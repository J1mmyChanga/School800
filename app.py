import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from data import db_session
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

api.add_resource(CompletedTasksResource, "/api/tasks/completed/<int:user_id>")
api.add_resource(InProcessTasksResource, "/api/tasks/processing/<int:user_id>")
api.add_resource(UndoneTasksResource, "/api/tasks/undone/<int:user_id>")

api.add_resource(GroupResource, "/api/groups")
api.add_resource(GroupPhotoResource, "/api/groups/images/<int:group_id>")

api.add_resource(KindsListResource, "/api/kinds")

api.add_resource(UsersListResource, "/api/users")
api.add_resource(UserResource, "/api/users/<int:user_id>")

api.add_resource(UserPhotoResource, "/api/users/images/<int:user_id>")
api.add_resource(AddingUserPhotoResource, "/api/users/images")

api.add_resource(MVUsersInGroup, "/api/mv_users_in_group/<int:group_id>")
api.add_resource(MVUsers, "/api/mv_users")


def main():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
