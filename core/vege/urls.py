from django.urls import path
from .views import *
urlpatterns = [
    path('read-receipe/', read_receipe, name="Read_Receipe"),
    path('delete/<int:id>', delete_receipe, name="delete_receipe"),
    path('', receipe, name="Receipe")
]
