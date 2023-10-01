# project_name/urls.py
from django.contrib import admin
from django.urls import path
from grade_dist_api_app import views  # Import views from your app

urlpatterns = [
    path('get_subject_codes/', views.get_subject_codes, name='get_subject_codes'),\
    path('', views.home, name='home'), 
    path('get_profs/<str:subject_code>/<str:course_code>/', views.get_profs, name = "get_profs")
]
