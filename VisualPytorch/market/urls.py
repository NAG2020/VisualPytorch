from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^market/$', views.modelList.as_view()),
    url(r'^market/(?P<pk>[0-9]+)/$', views.modelDetail.as_view()),
    url(r'^market/copy/(?P<pk>[0-9]+)$', views.modelDetail.post)
]
