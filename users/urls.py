from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from . import views

app_name = 'users'

urlpatterns = [
    # login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    #registration page
    path('register', views.register, name='register'),

]
