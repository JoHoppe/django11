from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate,login
from  django.http import HttpResponseRedirect
from django.contrib.auth.forms import  UserCreationForm


# Create your views here.
def register(request):
    """Register a new user"""
    if request.method != 'POST':
        #display blank reg page
        form = UserCreationForm()
        print("after blankform")

    else:
        #process completed form
        form= UserCreationForm(data=request.POST)
        print("before is valid")

        if form.is_valid():
            print("after is valid")
            new_user = form.save()
            #log the user in and redirect to homepage
            authenticated_user=authenticate(username=new_user.username,password =request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('django1app:index'))

    context={'form': form}
    return render(request, 'users/register.html', context)