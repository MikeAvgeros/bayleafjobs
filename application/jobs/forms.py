from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, TextAreaField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import InputRequired, DataRequired, Length


class JobForm(FlaskForm):
	company			= StringField("Company *",
								validators=[
									InputRequired("Input is required!"),
									DataRequired("Data is required!"),
									Length(min=5, max=50, message="Company must be between 5 and 50 characters long")
								])
	company_logo	= URLField("Company Logo")
	position		= StringField("Position *",
								validators=[
									InputRequired("Input is required!"),
									DataRequired("Data is required!"),
									Length(min=5, max=50, message="Position must be between 5 and 50 characters long")
								])
	stack			= SelectField("",
								choices=[
									("      ", "      "),
									("Front End", "Front End"), 
									("Back End", "Back End"), 
									("Full Stack", "Full Stack")],
								validators=[
									InputRequired("Input is required!"),
									DataRequired("Data is required!")
								])
	description 	= TextAreaField("Description *",
								validators=[
									InputRequired("Input is required!"),
									DataRequired("Data is required!"),
									Length(min=10, max=500, message="Description must be between 10 and 500 characters long")
								])
	responsibilities 	= TextAreaField("Responsibilities *",
									validators=[
										InputRequired("Input is required!"),
										DataRequired("Data is required!"),
										Length(min=10, max=500, message="Responsibilities must be between 10 and 500 characters long")
									])
	requirements 	= TextAreaField("Requirements *",
									validators=[
										InputRequired("Input is required!"),
										DataRequired("Data is required!"),
										Length(min=10, max=500, message="Requirements must be between 10 and 500 characters long")
									])
	salary			= StringField("Salary")
	location		= StringField("Location *",
								validators=[
									InputRequired("Input is required!"),
									DataRequired("Data is required!"),
									Length(min=3, max=40, message="Location must be between 3 and 40 characters long")
								])
	contract		= SelectField("",
								choices=[
									("         ", "         "),
									("Full Time", "Full Time"), 
									("Part Time", "Part Time"), 
									("Freelance", "Freelance")],
								validators=[
									InputRequired("Input is required!"),
									DataRequired("Data is required!")
								])
	level			= SelectField("",
								choices=[
									("      ", "      "),
									("Senior", "Senior"), 
									("Midweight", "Midweigth"), 
									("Associate", "Associate")],
								validators=[
									InputRequired("Input is required!"),
									DataRequired("Data is required!")
								])


class CreateJobForm(JobForm):
	submit 		= SubmitField("Create job")


class UpdateJobForm(JobForm):
	submit 		= SubmitField("Update job")


class ApplicationForm(FlaskForm):
	notice_period	= StringField("Notice Period *",
								validators=[
									InputRequired("Input is required!"),
									DataRequired("Data is required!"),
									Length(min=3, max=20, message="Notice period must be between 3 and 20 characters long")
								])
	current_salary	= StringField("Current Salary *",
								validators=[
									InputRequired("Input is required!"),
									DataRequired("Data is required!"),
									Length(min=3, max=20, message="Salary must be between 3 and 20 characters long")
								])
	desired_salary	= StringField("Desired Salary *",
								validators=[
									InputRequired("Input is required!"),
									DataRequired("Data is required!"),
									Length(min=3, max=20, message="Salary must be between 3 and 20 characters long")
								])
	resume			= URLField("Resume URL *",
								validators=[
									InputRequired("Input is required!"),
									DataRequired("Data is required!")
								])
	cover_letter	= URLField("Cover Letter URL")
	submit 			= SubmitField("Apply")
