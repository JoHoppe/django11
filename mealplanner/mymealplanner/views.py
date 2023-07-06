from django.shortcuts import render

# Create your views here.
def index(request):
    """the homepage for my mealplanner"""
    return render(request,"mymealplanner/index.html")
