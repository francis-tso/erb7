from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from listings.models import Listing

def index(request):
    listings = Listing.objects.filter(is_published=True)[:3]
    context = {"listings" : listings}
    return render(request, 'pages/index.html', context) 

def about(request):
    print(request.path)
    return render(request, 'pages/about.html')