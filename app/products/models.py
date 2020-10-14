from django.db import models

# Create your models here.


class Proveedor(models.Model):
    nombre = models.CharField(max_length=300)
    feactured = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'proveedores'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'proveedores'
        ordering = ['id']


class Producto(models.Model):
    nombre = models.CharField(max_length=300)
    slug = models.SlugField()
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='producto/', blank=True, verbose_name = 'Imagen')
    Descripcion = models.CharField(max_length=300, verbose_name='Descripcion del producto')
    Descuento = models.PositiveIntegerField(default=0)
    precio = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural ='Productos'
        ordering =['id']



