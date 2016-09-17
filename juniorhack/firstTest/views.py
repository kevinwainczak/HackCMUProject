#from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt 

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .form import PersonForm
from .models import *

@csrf_exempt
def get_name(request):
	if request.method == 'POST':
		form1 = PersonForm(request.form)
		if form1.is_valid():
			#return 
			name=PersonForm.your_name
			gender = PersonForm.your_gender
			age = PersonForm.your_age
			race = PersonForm.your_race
			sexuality = PersonForm.your_sexuality
			createPerson(name,gender,age,race,sexuality)
			return HttpResponse('Hi')
			#return redirect('/convo/')
	else:
		form1 = PersonForm()

	return render(request, 'name.html', {'form':form1})


def index(request):
	return render(request, 'index.html')
	#("Hello, world. You're at the polls index.")

#def welcome(request):
#	return render(request, 'welcome.html', {'form':form0})

