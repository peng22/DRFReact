from django.urls import path, include
from .views import *
urlpatterns = [
    path('constructions',Construction_list.as_view(),name='Construction_list'),
    path('constructions/<int:pk>',Construction_details.as_view(),name='Construction_details'),
    path('Engineers',Engineer_list.as_view(),name='Engineer_list'),
    path('Engineers/<int:pk>',Engineer_details.as_view(),name='Engineer_details'),
    path('constructions/<int:pk>/Engineers',Construction_Engineers.as_view(),name='Construction_Engineers')




]
