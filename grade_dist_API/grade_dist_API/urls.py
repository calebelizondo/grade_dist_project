# project_name/urls.py
from django.contrib import admin
from django.urls import path, include
from grade_dist_api_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('grade_dist_api_app.urls')),  # Include your app's URLs under 'api/'
]