import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = '878436c0a462c4145fa59eec2c43a66a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_BINDS'] = {'users':'sqlite:///users.db','packages':'sqlite:///packages.db','repo':'sqlite:///repo.db'}
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from pushsqrepo import routes