from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('download/<str:filename>/', views.download_file, name='download_file')
]