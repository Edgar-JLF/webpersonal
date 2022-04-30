from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name = 'about'),
    path('courses/', views.courses, name = 'courses')
]