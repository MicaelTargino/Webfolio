from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero, Contact, Portfolio, Skills, About
# Create your views here.
def home(request):
    hero = Hero.objects.all().first()
    contact = Contact.objects.all().first()
    portfolio = Portfolio.objects.all().first()
    skills = Skills.objects.all().first()
    about = About.objects.all().first()
    return render(request, 'home.html', {
        'sections': {
    	    'hero': hero,
            'contact': contact,
            'portfolio': portfolio,
            'skills': skills,
            'about': about
        },
        'known_icons': {
            'Email': 'fa fa-envelope',
            'email': 'fa fa-envelope',
            'gmail': 'fa fa-envelope',
            'Gmail': 'fa fa-envelope'
        }
    })