import os
from flask import render_template, url_for, flash, redirect, request, abort, session,jsonify
from pushsqrepo import app, db, bcrypt
from pushsqrepo.models import User,Repo,Packages
from pushsqrepo.forms import Search_Package_Repo_Form
from pushsqrepo.check import Check
import json
import pathlib
import shutil


#Home Page Repository
@app.route('/')
def home():
	form = Search_Package_Repo_Form()
	len_repo = len(Repo.query.all())
	len_packages = len(Packages.query.all())

	return render_template('home.html',title='Search',form=form,len_repo=len_repo,len_packages=len_packages)


#Validate Adim pass
@app.route('/validate_admin_pass',methods=['POST'])
def validate_admin_pass():
	data = request.get_json()
	checkobj = Check()
	result = checkobj.validateadminpass(data['adminpass'])
	return result

#Validate Repository name
@app.route('/validate_repo_name',methods=['POST'])
def validate_repo_name():
	data = request.get_json()
	checkobj = Check()
	result = checkobj.validatereponame(data['reponame'])
	return result

#Create new Repository
@app.route('/create_new_repo',methods=['POST'])
def create_new_repo():
	data = request.get_json()
	checkobj = Check()
	result = checkobj.createnewrepo(data['reponame'],data['category'])
	return result

#Search repository
@app.route('/search_repo',methods=['POST'])
def search_repo():
	data = request.get_json()
	checkobj = Check()
	result = checkobj.searchrepo(data['searchreponame'])
	return result

#Delete Repo
@app.route('/delete_repo',methods=['POST'])
def delete_repo():
	data = request.get_json()
	checkobj = Check()
	result = checkobj.deleterepo(data['reponame'])