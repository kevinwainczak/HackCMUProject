from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^i$', views.index, name='index'),
    url(r'^name$', views.get_name, name='name'),
]

#from django.conf.urls import url

#from firstTest import views

#urlpatterns = [
#	url(r'^$', views.index, name='index'),
#]
