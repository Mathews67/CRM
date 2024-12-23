# homeaffairs/urls.py (main project's urls.py)
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('crm.urls')),  # Include crm's URLs for API endpoints like login
]
