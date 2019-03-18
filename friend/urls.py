from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[    
    url(r'^$',views.home,name="home"),
    url(r'^create',views.createquestionnaire,name="build"),
    url(r'^answer/(\w+)',views.filling,name="filling")

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
