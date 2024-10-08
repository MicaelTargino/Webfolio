from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero, Contact, Portfolio, Skills, About, Aside, ThemeColors, CV

# Create your views here.
def home(request):
    hero = Hero.objects.all().first()
    contact = Contact.objects.all().first()
    portfolio = Portfolio.objects.all().first()
    skills = Skills.objects.all().first()
    about = About.objects.all().first()
    aside = Aside.objects.all().first()
    theme_colors = ThemeColors.objects.first()
    dark_or_light = 'dark' if theme_colors.dark_mode else 'light'
    return render(request, 'home.html', {
        'sections': {
    	    'hero': hero,
            'contact': contact,
            'portfolio': portfolio,
            'skills': skills,
            'about': about,
            'aside': aside,
            'theme_colors': theme_colors
        },
        'style': {
            'dark_or_light': dark_or_light
        },
        'known_icons': {
            'Email': 'fa fa-envelope',
            'email': 'fa fa-envelope',
            'gmail': 'fa fa-envelope',
            'Gmail': 'fa fa-envelope'
        }
    })