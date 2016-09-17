from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^i$', views.index, name='index'),
    url(r'^name$', views.get_name, name='name'),
    url(r'^update$', views.updateArray, name='update array')
    url(r'^result$', views.mapResult, name='mapResult')
    url(r'^finalResult$', views.res, name='finalResult')
]

#from django.conf.urls import url

#from firstTest import views

updateArray
results

#urlpatterns = [
#	url(r'^$', views.index, name='index'),
#]
