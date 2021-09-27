from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('api/', include(router.urls))             
]
