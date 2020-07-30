from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new_job),
    path('dashboard', views.dashboard),
    path('register', views.register),
    path('save/job', views.create_job),
]
