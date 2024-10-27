from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("excercises/", views.excercises, name="excercises"),
]
