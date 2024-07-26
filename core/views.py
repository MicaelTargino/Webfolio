from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero
# Create your views here.
def home(request):
    hero = Hero.objects.all().first()
    print(hero.name)
    return render(request, 'home.html', {
        'sections': {
    	    'hero': hero
        }
    })