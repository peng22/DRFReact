from django.shortcuts import render

# Create your views here.
from .serializers import TodoSerializer 
from rest_framework import viewsets
from .models import Todo

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
