from django.conf import settings
from django.urls import path
from webapp.views import *
from django.conf.urls.static import static


app_name = 'webapp'


urlpatterns = [
    path('', index, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)