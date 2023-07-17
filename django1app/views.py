from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic,Entry
from .forms import TopicForm,EntryForm

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

def new_topic(request):
    """add a new topic"""
    if request.method != 'POST':
        #No data submitted; create a blank form
        form = TopicForm()
    else:
        #Post data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('django1app:topics'))

    context = {'form': form}
    return render(request, 'django1app/new_topic.html', context)
def new_entry(request,topic_id):
    """add a new entry linked to a topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #no data was entered,create blank+
        form=EntryForm()

    else:
        #post data submitted, process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('django1app:topic',args=[topic_id]))

    context={'topic':topic,'form':form}
    return render(request, 'django1app/new_entry.html', context)

def edit_entry(request,entry_id):
    """edit an existing entry"""
    entry= Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        #get the current entry to then be able to edit it
        form= EntryForm(instance=entry)

    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('django1app:topic', args=[topic.id]))

    context ={'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'django1app/edit_entry.html', context)
