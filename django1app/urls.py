"""Defines the url patterns for django1app"""

from django.urls import path
from . import views

app_name = "django1app"
urlpatterns=[
    #home page
    path("",views.index,name="index"),

    #show all topics
    path("topics/", views.topics,name="topics"),
]