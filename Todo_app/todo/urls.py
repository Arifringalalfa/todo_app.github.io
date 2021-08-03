

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('deleteTask/<int:pk>',views.deleteTask,name="deleteTask")
]