from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('chinese_hsk/', include('chinese_hsk.urls')),  # Assuming chinese_hsk has its own urls.py
]
