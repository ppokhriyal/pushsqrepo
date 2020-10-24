from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField,RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



#Search Package repository
class Search_Package_Repo_Form(FlaskForm):
	name = StringField('Name',validators=[DataRequired(),Length(min=2,max=20)])
	search_on = RadioField('Search',choices=[('packages','Packages'),('repo','Repository')],default='packages')
	submit = SubmitField('Search')