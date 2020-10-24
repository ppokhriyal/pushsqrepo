from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from pushsqrepo import db, app



class User(db.Model):
	__bind_key__ = 'users'
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	email = db.Column(db.String(120),unique=True,nullable=False)
	password = db.Column(db.String(60),nullable=False)
	repos = db.relationship('Repo',backref='user')
	pkgs = db.relationship('Packages',backref='user')

	def __repr__(self):

		return f"User('{self.username}','{self.email}')"

class Repo(db.Model):
	__bind_key__ = 'repo'
	id = db.Column(db.Integer,primary_key=True)
	repo_name = db.Column(db.String(20),unique=True,nullable=False)
	repo_category = db.Column(db.String(20),nullable=False,default='misc')
	repo_creation_date = db.Column(db.DateTime(),nullable=False,default=datetime.now)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
	pkgs = db.relationship('Packages',backref='repo')

	def __repr__(self):
		return f"Repo('{self.repo_name}')"

class Packages(db.Model):
	__bind_key__ = 'packages'
	id = db.Column(db.Integer,primary_key=True)
	pkg_name = db.Column(db.String(20),unique=True,nullable=False)
	pkg_creation_date = db.Column(db.DateTime(),nullable=False,default=datetime.now)
	pkg_size = db.Column(db.String(20),unique=True,nullable=False)
	pkg_category = db.Column(db.String(20),nullable=False,default='misc')
	pkg_arch = db.Column(db.String(20),nullable=False,default='amd64')
	repo_id = db.Column(db.Integer,db.ForeignKey('repo.id'))
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

	def __repr__(self):
		return f"Packages('{self.pkg_name}')"