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
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'jfif'}

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


@app.route('/api/users/images', methods=['POST'])
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
        file.save(os.path.join(f"{app.config['UPLOAD_FOLDER']}", filename))


@app.route('/api/users/images/<string:user_uid>', methods=['GET'])
def download_file(user_uid):
    print(user_uid)
    session = db_session.create_session()
    user = session.get(Users, user_uid)
    print(user)
    print(app.config["UPLOAD_FOLDER"])
    print(user.image)
    return send_from_directory(app.config["UPLOAD_FOLDER"], user.image)


def main():
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(port=8080, host='0.0.0.0')


if __name__ == '__main__':
    main()
