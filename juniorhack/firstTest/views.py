#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

from .form import PersonForm

def get_name(request):
	if request.method == 'POST':
		form1 = PersonForm(request.POST)
		if form1.is_valid():
			return HttpResponse('/thanks/')
	else:
		form1 = PersonForm()

	return render(request, 'name.html', {'form':form1})


def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")