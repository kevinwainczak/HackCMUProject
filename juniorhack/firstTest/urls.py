from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^name$', views.get_name, name='get_name'),
    url(r'^loading$', views.wait, name='wait'),
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
