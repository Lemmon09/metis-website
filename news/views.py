from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from news.models import CurrentEvent

# Create your views here.
def index(request):
    context = {'news': 'this is my news, cool huh?'}
    return render(request, 'news/index.html', context)
    
def aboutUs(request):
    context = {}
    return render(request, 'news/aboutUs.html', context)
    
def contactUs(request):
    return render(request, 'news/contactUs.html')
    
def services(request):
    return render(request, 'news/services.html')
    
class IndexView(generic.ListView):
    template_name = 'news/index.html'
    model = CurrentEvent
    context_object_name = 'news'
    
