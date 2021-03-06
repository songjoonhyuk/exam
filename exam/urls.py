from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$' , 'mall.views.index'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^mall/', include('mall.urls', namespace='mall')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

