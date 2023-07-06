from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """The home page for django1app"""
    return render(request,"django1app/index.html")

def topics(request):
    """Show all topics."""
    topics= Topics.objects.order_by("date_added")
    context={"topics":topics}
    return render(request,"learning_logs/topics.html",context)

