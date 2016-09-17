from django.conf.urls import url, include

from . import views
from modelInterface import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^name$', views.get_name, name='get_name'),
    url(r'^loading$', views.wait, name='wait'),
    url(r'^result$', views.checkForConvo, name='result'),
<<<<<<< HEAD
=======
    url(r'^getIndex$', view.getDistances, name='getIndex'),
>>>>>>> d48a60d0f0eab7cd1d13bf05b369b49b9f73357e
   # url(r'^convo$', views.convo, name='convo'),
 #   url(r'^update$', views.updateArray, name='update array')
 #   url(r'^result$', views.mapResult, name='mapResult')
 #   url(r'^finalResult$', views.res, name='finalResult')
]

#from django.conf.urls import url

#from firstTest import views

#updateArray
#results

#urlpatterns = [
#	url(r'^$', views.index, name='index'),
#]
