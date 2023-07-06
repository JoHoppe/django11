"""degine url patterns for my mealplanner app"""

from django.urls import path
from . import views

app_name = "mymealplanner"
urlpatterns =[
    path("",views.index, name="index"),
]