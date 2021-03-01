from django.contrib import admin
from django.urls import path, include
from . import web
from login import urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', web.home),
    path('home/', web.home),
    path('login/', include('login.urls')),
    path('logout/', web.logout_user),
    path('desktop/', web.desktop),
    path('accessory/', web.accessory),
    path('laptop/', web.laptop),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
