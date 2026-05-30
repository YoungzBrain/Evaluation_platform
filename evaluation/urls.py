from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('',              include('accounts.urls')),
    path('',              lambda request: redirect('login')),
    path('',              include('courses.urls')),      # ← AJOUTER
]
