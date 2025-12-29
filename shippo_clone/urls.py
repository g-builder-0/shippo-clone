"""
URL configuration for shippo_clone project.
"""
from django.contrib import admin
from django.urls import path, include

print(f"[🔍 PROJECT URLS] Main urls.py loading...")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rates.urls')),
]

print(f"[🔍 PROJECT URLS] URL patterns configured")