from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('process_order/', process_order, name='process_order'),
    path('me/', login_required(Order_list.as_view(), login_url="/autenticacion/login"), name='order_list'),

]
