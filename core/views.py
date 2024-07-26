from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero, Contact
# Create your views here.
def home(request):
    hero = Hero.objects.all().first()
    contact = Contact.objects.all().first()
    return render(request, 'home.html', {
        'sections': {
    	    'hero': hero,
            'contact': contact
        },
        'known_icons': {
            'Email': 'fa fa-envelope',
            'email': 'fa fa-envelope',
            'gmail': 'fa fa-envelope',
            'Gmail': 'fa fa-envelope'
        }
    })