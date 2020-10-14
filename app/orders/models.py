from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField
from products.models import Producto

User = get_user_model()

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.orderline_set.aggregate(
            total=Sum(F("producto__precio") * F("existencia"), output_field=FloatField())
        )["total"] or FloatField(0)

    def __str__(self):
        return self.id


    class Meta:
        db_table = 'orders'
        verbose_name = 'Pedido'
        verbose_name_plural = 'pedidos'
        ordering = ["id"]


class OrderLine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    existencia = models.IntegerField(default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.existencia} de {self.producto.nombre}'

    class Meta:
        db_table = 'orderlines'
        verbose_name = 'linea de pedido'
        verbose_name_plural = 'lineas de pedido'
        ordering = ['id']
