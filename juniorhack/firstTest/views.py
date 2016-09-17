#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .form import PersonForm
from .models import *

def get_name(request):
	if request.method == 'POST':
		form1 = PersonForm(request.form)
		if form1.is_valid():
			return 
			return HttpResponse('/thanks/')
	else:
		form1 = PersonForm()

	return render(request, 'name.html', {'form':form1})


def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def trial(request, question_id):
