
from django.contrib import admin 
from django.urls import path, include
from EmailCeleryService.views import index , send_mail_to_user, get_all_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('send-email/', send_mail_to_user, name='send_mail_to_user'),
    path('get-products/', get_all_products, name='get_all_products'),
]
