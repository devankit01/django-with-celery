from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from SendEmail.tasks import send_email_func, _get_products_list

# Create your views here.
def index(request):
    print("This is only for testing.")
    test_func.delay()
    return HttpResponse('Done')


def send_mail_to_user(request):
    send_email_func.delay()
    return HttpResponse('Sent')


def get_all_products(request):
    _get_products_list.delay()
    return HttpResponse('Get Products Data')

