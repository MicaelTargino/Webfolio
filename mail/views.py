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
            return JsonResponse(data={'status': 400, 'message':'Invalid Data'})
        
        name = data.get('name', '')
        email = data.get('email', '')
        body = data.get('body', '')

        if not (name and email and body):
            if not name:
                return JsonResponse(data={'status': 400, 'message':'Name field is required'})
            if not email:
                return JsonResponse(data={'status': 400, 'message':'Email field is required'})
            if not body:
                return JsonResponse(data={'status': 400, 'message':'Message field is required'})
        
        subject = data.get('subject', f'email from {name}')

        send_email(name, email, subject, body)
        return JsonResponse({'status': 200, 'message': 'Email sent successfully'})
    
    return HttpResponseBadRequest('Invalid request method')