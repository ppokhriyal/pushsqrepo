import os
from flask import Flask,request,abort,flash,redirect,url_for,jsonify
from werkzeug.utils import secure_filename
import json
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

UPLOAD_FOLDER = '/var/www/html/flask_upload'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','sq','SQ'}

#App Config
app = Flask(__name__)
app.config['SECRET_KEY'] = '878436c0a462c4145fa59eec2c43a66a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/webhook',methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return '',200
    else:
        abort(400)

@app.route('/upload/<int:id>',methods=['POST'])
def upload_files(id) -> str:
    submitted_file = request.files['file']

    if submitted_file:
        filename = secure_filename(submitted_file.filename)
        directory = os.path.join(app.config['UPLOAD_FOLDER'], str(id))
        if not os.path.exists(directory):
            os.mkdir(directory)
        submitted_file.save(os.path.join(directory, filename))
        out = {'status': 'HTTPStatus.OK','filename': filename,'message': f"{filename} saved successful."}

        return jsonify(out)

@app.route('/validate_username',methods=['POST'])
def validate_username():

    data = request.get_json()
    username = data['username']
    return jsonify({'result':'success','username':username})


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
