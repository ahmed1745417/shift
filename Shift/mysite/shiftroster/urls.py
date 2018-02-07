from django.conf.urls import url

from . import views

app_name = 'shiftroster'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^generate$', views.generate, name='generate'),
    url(r'^calculate$', views.calculate, name='calculate'),
    url(r'^exchange$', views.exchange, name='exchange'),
    url(r'^leave$', views.leave, name='leave'),
    url(r'^test$', views.test, name='test'),
    url(r'^home$', views.home, name='home'),
    url(r'^results$', views.ResultsView.as_view(), name='results')
]
