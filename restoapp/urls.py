from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.resto,name='resto'),
    url(r'^locations/', views.resto_location,name='locations'),
    url(r'search/',views.search_resto,name='search_resto')
]
# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)