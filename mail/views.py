from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponseBadRequest
from .utils import send_email
# Create your views here.

def send_mail(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON payload')
        name = data.get('name', '')
        email = data.get('email', '')
        subject = data.get('subject', '')
        body = data.get('body', '')

        if not (name and email and subject and body):
            return HttpResponseBadRequest('All fields are required')

        send_email(name, email, subject, body)
        return JsonResponse({'message': 'Email sent successfully'})
    
    return HttpResponseBadRequest('Invalid request method')