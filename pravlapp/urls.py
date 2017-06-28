from django.conf.urls import url
from pravlapp.api import user_api

urlpatterns = [
    url(r'^users', user_api.UserDetail.as_view()),
    url(r'^login', user_api.Authentication.as_view())
]