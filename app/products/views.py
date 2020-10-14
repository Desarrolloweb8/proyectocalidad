from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto
from cart.cart import Cart

# Create your views here.


@login_required(login_url='autenticacion/acceder')
def listado_productos(request):
    cart = Cart(request)
    productos = Producto.objects.all()
    return render(request,"products/listado.html", {
        "productos": productos
    })

