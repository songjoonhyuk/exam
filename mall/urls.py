from django.conf.urls import url

urlpatterns = [
	url(r'^(?P<pk>\d+)/$', 'mall.views.category_detail', name='category_detail'),
	url(r'^(?P<category_pk>\d+)/(?P<pk>\d+)/$', 'mall.views.shop_detail', name='shop_detail'),
]