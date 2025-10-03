from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from listings.models import Listing
from doctors.models import Doctor

def index(request):
    listings = Listing.objects.filter(is_published=True)[:3]
    context = {"listings" : listings}
    return render(request, 'pages/index.html', context) 

def about(request):
    #print(request.path)
    doctors = Doctor.objects.order_by("-hire_date")[:3]
    mvp_doctors =Doctor.objects.all().filter(is_mvp=True)
    context = {
        "doctors": doctors,
        "mvp_doctors" : mvp_doctors
    }
    return render(request, 'pages/about.html', context)