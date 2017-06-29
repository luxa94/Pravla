from django.conf.urls import url
from pravlapp.api import user_api, firebase_token_api, device_api

urlpatterns = [
    url(r'^users', user_api.UserDetail.as_view()),
    url(r'^login', user_api.Authentication.as_view()),
    url(r'^tokens', firebase_token_api.FirebaseTokenDetail.as_view()),

    url(r'devices', device_api.DeviceList.as_view())
]