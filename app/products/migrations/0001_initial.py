# Generated by Django 3.1.1 on 2020-10-02 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('feactured', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'proveedores',
                'db_table': 'proveedores',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, upload_to='producto/', verbose_name='Imagen')),
                ('Descripcion', models.CharField(max_length=300, verbose_name='Descripcion del producto')),
                ('Descuento', models.PositiveIntegerField(default=0)),
                ('precio', models.PositiveIntegerField(default=0)),
                ('available', models.BooleanField(default=True)),
                ('fecha_alta', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.proveedor')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'productos',
                'ordering': ['id'],
            },
        ),
    ]
