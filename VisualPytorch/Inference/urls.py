from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^resnet18/$', views.InferenceList.as_view()),
]