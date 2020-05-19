from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^comments/$', views.CommentList.as_view()),
    # url(r'^comments1/$', views.upload_handle),
]