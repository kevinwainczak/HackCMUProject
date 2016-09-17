#from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .form import PersonForm
from .models import *
from .modelInterface import createPerson


@csrf_exempt
def get_name(request):
	if request.method == 'POST':
		form1 = PersonForm(request.POST)
		if form1.is_valid():
			print(form1.cleaned_data.items())
			#return
			print(form1.cleaned_data)
			name=form1.cleaned_data['your_name']
			gender = form1.cleaned_data['your_gender']
			age = form1.cleaned_data['your_age']
			race = form1.cleaned_data['your_race']
			sexuality = form1.cleaned_data['your_sexuality']
			topic = form1.cleaned_data['your_topic']
			roast = form1.cleaned_data['your_roast']
			distance = request.POST['distance']
			#distance = '3';# distace.cleaned_data['distance'];
			createPerson(name,gender,age,race,sexuality,roast,topic,distance) #location & topic?
			#return HttpResponse('Hi')
			return redirect('wait')
	else:
		form1 = PersonForm()

	return render(request, 'name.html', {'form':form1})

def checkForConvo():
    convo = []
    allElements = Person.objects.all()
    if len(allElements) < 3: return "no"
    for person in allElements:
        flag = 0
        for x in convo:
            if demographicEqual(person, x):
                flag = 1
        if flag == 0:
            convo.append(person)
        if len(convo) == 3:
            break
    return "yes"

def checkForConvo():
    convo = []
    allElements = Person.objects.all()
    if len(allElements) < 3: return "no"
    for person in allElements:
        flag = 0
        for x in convo:
            if demographicEqual(person, x):
                flag = 1
        if flag == 0:
            convo.append(person)
        if len(convo) == 3:
            break
    return "yes"

def findIndex(a):
    x1 = a[0].split(',')
    y1 = a[1].split(',')
    z1 = a[2].split(',')
    arr = range(len(x1))
    for i in xrange(len(x1)):
        a[i] = x1[i] + y1[i] + z1[i]
    minIndex = a.index(min(a))
    return minIndex

def getDistances():
    convo = []
    allElements = Person.objects.all()
    for person in allElements:
        flag = 0
        for x in convo:
            if demographicEqual(person, x):
                flag = 1
        if flag == 0:
            convo.append(person)
        if len(convo) == 3:
            break
    result = (convo[0].distance, convo[1].distance, convo[2].distance)
    return findIndex(result)

def index(request):
	return render(request, 'index.html')
	#("Hello, world. You're at the polls index.")

def wait(request):
	return render(request, 'wait.html')
#def welcome(request):
#	return render(request, 'welcome.html', {'form':form0})
