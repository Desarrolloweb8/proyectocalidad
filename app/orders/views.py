from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Order, OrderLine
from cart.cart import Cart


# Create your views here.

@login_required(login_url='/autenticacion/acceder')
def process_order(request):
    order = Order.objects.create(user=request.user, completed=True)
    cart = Cart(request)
    order_lines = list()
    for key, value in cart.cart.items():
        order_lines.append(
            OrderLine(
                producto_id=key,
                existencia=value["existencia"],
                user=request.user,
                order=order

            )
        )

    OrderLine.objects.bulk_create(order_lines)

    send_order_email(
        order=order,
        order_lines=order_lines,
        username=request.user.username,
        user_email=request.user.email

    )
    messages.success(request, "el pedido se a creado correctamente")
    return redirect("listado_productos")


def send_order_email(**kwargs):
    subject = "gracias por tu pedido"
    html_message = render_to_string("emails/nuevo_pedido.html", {
        "order": kwargs.get("order"),
        "order_lines": kwargs.get("order_lines"),
        "username": kwargs.get("username")
    })
    plain_message = strip_tags(html_message)
    from_email = "margiorybart@gmail.com"
    to = kwargs.get("user_email")
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

class Order_list(ListView):
    model = Order
    ordering = ["-id"]
    template_name = "orders/listado.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)