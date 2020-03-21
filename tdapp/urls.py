from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('add_todo', views.add_todo),
    path('text_delete/<int:todo_id>/', views.text_delete),
]