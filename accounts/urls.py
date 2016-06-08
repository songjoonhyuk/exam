from django.conf.urls import url
from django.contrib.auth.views import login, logout
from accounts import views

urlpatterns = [
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login/$', login, name='login'),
	url(r'^login/$', logout, name='logout'),
	url(r'^profile/$', views.profile, name='profile'),
]