from django.conf.urls import url

urlpatterns = [
	url(r'^(?P<pk>\d+)/$', 'mall.views.category_detail', name='category_detail'),
]