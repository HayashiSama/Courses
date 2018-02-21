# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.db import IntegrityError
from models import *
import random
import datetime
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):

	courselist = Course.objects.all()
	context = { 'courses':courselist}
	print context
	return render(request, 'courses_app/index.html', context)

def addcourse(request):
	if request.method=='POST':
		errors = {}
		errors = Course.objects.basic_validator(request.POST)
		if(len(errors)):
			print errors
			return redirect('/courses_app')

		name = request.POST['name']
		desc = request.POST['desc']

		try:
			Course.objects.create(name=name, desc=desc)
		except IntegrityError as e:
			if 'error' in e.message:
				print "ERROR"
		return redirect('/courses_app')

def destroy(request, id):
	try:
		b = Course.objects.get(id=id)
	except User.DoesNotExist:
		print "Course DOES NOT EXIST"
		return redirect ("/courses_app")
	b.delete() # deletes that particular record	
	return redirect ("/courses_app")