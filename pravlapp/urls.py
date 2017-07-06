from django.conf.urls import url
from pravlapp.api import user_api, firebase_token_api, device_api, message_api, rule_api
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^users$', user_api.UserDetail.as_view()),
    url(r'^login$', user_api.Authentication.as_view()),
    url(r'^tokens$', firebase_token_api.FirebaseTokenDetail.as_view()),
    url(r'^devices$', device_api.DeviceList.as_view()),
    url(r'^devices/(?P<pk>[0-9]+)$', device_api.DeviceDetail.as_view()),
    url(r'^messages$', message_api.MessageList.as_view()),
    url(r'^rules$', rule_api.RuleList.as_view()),
    url(r'^rules/(?P<pk>[0-9]+)$', rule_api.RuleDetails.as_view())
]

urlpatterns += staticfiles_urlpatterns()
