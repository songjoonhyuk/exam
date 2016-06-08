from django.conf.urls import url
from django.contrib.auth.views import login, logout
from accounts import views

urlpatterns = [
	url(r'^signup/$', views.signup),
]