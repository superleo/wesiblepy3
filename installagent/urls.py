from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.test, name='test'),
    url(r'^install1node$', views.install1node, name='install1node'),
]

