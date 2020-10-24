from flask import jsonify
import pathlib
import shutil
import os
from pushsqrepo import app, db, bcrypt
from pushsqrepo.models import User,Repo,Packages


class Check():
	def __init__(self):

		print("init called")

	def validateadminpass(self,adminpass):

		admin_db = User.query.filter(User.password==adminpass).first()

		if admin_db:
			return f"pass"
		else:
			return f"fail"
		

	def validatereponame(self,reponame):

		repo_db = Repo.query.filter_by(repo_name=reponame).first()

		if repo_db == None:
			return f"fail"
		else:
			return f"pass"

	def createnewrepo(self,reponame,category):
		os.makedirs('/var/lib/pushsqrepo/repo/repo:'+reponame,exist_ok=True)
		try:
			adminuser = User.query.filter_by(username='admin').first()
			repo_db = Repo(repo_name=reponame,repo_category=category,user=adminuser)
			db.session.add(repo_db)
			db.session.commit()
			return f"pass"
		except Exception as e:
			shutil.rmtree('/var/lib/pushsqrepo/repo/repo:'+reponame)
			return f"fail"

	def searchrepo(self,reponame):
		
		result_dict = {}
		repo_db = Repo.query.filter(Repo.repo_name.like(f'%{reponame}%')).all()
		len_repo_search = len(repo_db)

		for i in repo_db:
			result_dict[i.repo_name] = i.repo_category

		return jsonify({'Total search result':len_repo_search,'Result':result_dict})

	def deleterepo(self,reponame):
		repo_db = Repo.query.filter_by(repo_name=reponame).first()
		db.session.delete(repo_db)
		db.session.commit()

		#Remove repo directory
		shutil.rmtree('/var/lib/pushsqrepo/repo/repo:'+reponame)
		
		return f"pass"
