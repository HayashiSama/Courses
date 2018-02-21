  # Inside models.py
from __future__ import unicode_literals
from django.db import models
from django.core.validators import EmailValidator

class Course(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField()	
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)