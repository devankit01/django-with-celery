from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celery import shared_task
import requests
from .models import Product

@shared_task(bind =True)
def send_email_func(self):
    # Operations

    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Hey, Celery"
        message = "I am a Message"
        to_email = user.email
        for _ in range(2):
            resp = send_mail(
                subject=mail_subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[to_email],
                fail_silently=False
            )
            print(resp)
    return "Done"


@shared_task(bind =True)
def _get_products_list(self):
    url = 'https://api.escuelajs.co/api/v1/products'
    response = requests.get(url=url)
    response_json = response.json()
    for product in response_json:
        Product.objects.create(title=product['title'], description = product['description'], image = product.get('image', None), price = product['price'])
    return "Saved Products List Task Finished"