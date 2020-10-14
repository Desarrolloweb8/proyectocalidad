from django.urls import path
from .views import *

app_name = "cart"

urlpatterns = [
    path('add_product/<int:producto_id>', add_producto, name='add_producto'),
    path('remove_product/<int:producto_id>', remove_producto, name='remove_producto'),
    path('decrement_product/<int:producto_id>', decrement_producto, name='decrement_producto'),
    path('clear', clear_cart, name='clear_cart'),


]
