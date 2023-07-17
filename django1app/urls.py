"""Defines the url patterns for django1app"""

from django.urls import path
from . import views

app_name = "django1app"
urlpatterns=[
    #home page
    path("",views.index,name="index"),

    #show all topics
    path("topics/", views.topics,name="topics"),
    #detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Page for adding new Topics
    path('new_topic/', views.new_topic, name='new_topic'),
    #page for adding new Entries
    path('new_entry/<int:topic_id>/', views.new_entry,name ='new_entry' ),
    #page for editing entries
    path('edit_entry/<int:entry_id>/', views.edit_entry, name ='edit_entry'),

]