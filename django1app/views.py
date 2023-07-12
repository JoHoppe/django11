from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """The home page for django1app"""
    return render(request,"django1app/index.html")

def topics(request):
    """Show all topics."""
    topics= Topic.objects.order_by("date_added")
    context={"topics":topics}
    return render(request, "django1app/topics.html", context)

def topic(request, topic_id):
    """shows a single topic all its entries"""
    topic= Topic.objects.get(id=topic_id)
    entries= topic.entry_set.order_by("-date_added")
    """the - reverses the order, so most recent first"""
    context = {"topic" : topic, "entries" : entries}
    return render(request, "django1app/topic.html", context)

