from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login),
    path('signup/', views.signup),
    path('signup/save/', views.save),
    path('login_useer/', views.login_useer)
]
