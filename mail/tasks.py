from celery import shared_task
from .utils import send_email

@shared_task
def send_email_task(name, email, subject, body):
    send_email(name, email, subject, body)