from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
User = get_user_model()

class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ( 'GET',"POST", 'PUT', 'DELETE','PATCH','HEAD', 'OPTIONS') and request.user.id in [1000,1001,1002,1004,1006,1000]:
            return True
        return False

class Engineer_list(generics.ListCreateAPIView):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer
    # permission_classes = (CustomPermission,)


class Engineer_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer
    # permission_classes = (CustomPermission,)

# @api_view(['GET', 'POST'])
# def Construction_Engineers(request,pk):
#     construction=Construction.objects.get(id=pk)
#     Engineers=Engineer.objects.filter(place__contained=construction.shape)
#     print(EngineerSerializer.serialize(Engineers))
#
#     return Response({"message": "Hello, world!"})

class Construction_Engineers(generics.ListAPIView):
    serializer_class = EngineerSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['pk']
        construction=Construction.objects.get(id=pk)
        queryset=Engineer.objects.filter(place__contained=construction.shape)
        # print(Engineers)
        return queryset


class Construction_list(generics.ListCreateAPIView):
    queryset = Construction.objects.all()
    serializer_class = ConstructionSerializer
    # permission_classes = (CustomPermission,)


class Construction_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Construction.objects.all()
    serializer_class = ConstructionSerializer
    # permission_classes = (CustomPermission,)


class Cement_Supply_list(generics.ListCreateAPIView):
    queryset = Cement_Supply.objects.all()
    serializer_class = Cement_SupplySerializer
    # permission_classes = (CustomPermission,)


class Cement_Supply_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cement_Supply.objects.all()
    serializer_class = Cement_SupplySerializer
    # permission_classes = (CustomPermission,)

class Water_Supply_list(generics.ListCreateAPIView):
    queryset = Water_Supply.objects.all()
    serializer_class = Water_SupplySerializer
    # permission_classes = (CustomPermission,)


class Water_Supply_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Water_Supply.objects.all()
    serializer_class = Water_SupplySerializer
    # permission_classes = (CustomPermission,)

class Brick_Supply_list(generics.ListCreateAPIView):
    queryset = Brick_Supply.objects.all()
    serializer_class = Brick_SupplySerializer
    # permission_classes = (CustomPermission,)


class Brick_Supply_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brick_Supply.objects.all()
    serializer_class = Brick_SupplySerializer
    # permission_classes = (CustomPermission,)
