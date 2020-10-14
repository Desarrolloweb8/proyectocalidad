from django.shortcuts import render,redirect
from products.models import Producto
from django.contrib.auth.decorators import login_required
from .cart import Cart

# Create your views here.


@login_required(login_url="/autenticacion/login")
def add_producto(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.add(producto=producto)
    return redirect("listado_productos")


@login_required(login_url="/autenticacion/login")
def remove_producto(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.remove(producto)
    return redirect("listado_productos")


@login_required(login_url="/autenticacion/login")
def decrement_producto(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.decrement(producto=producto)
    return redirect("listado_productos")


@login_required(login_url="/autenticacion/login")
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("listado_productos")