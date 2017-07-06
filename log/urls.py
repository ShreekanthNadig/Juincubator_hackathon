#!python
# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.about, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^postdata$', views.postdata, name='postdata'),
]
