  # Inside models.py
from __future__ import unicode_literals
from django.db import models
from django.core.validators import EmailValidator


class CourseManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['name'])<5:
			errors['name'] = "Course name should be more than 5 character"
		if len(postData['desc'])<10:
			errors['desc'] = "Course desc should be more than 10 character"
		return errors

class Course(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField()	
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects=CourseManager()

