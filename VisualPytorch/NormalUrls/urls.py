from django.conf.urls import url
from NormalUrls import views

urlpatterns = [
    url('index', views.index)
]