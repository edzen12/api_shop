# Generated by Django 3.2.5 on 2021-08-29 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-id',), 'verbose_name': 'Продукт Артикул', 'verbose_name_plural': 'Продукты Артикулы'},
        ),
        migrations.AlterModelOptions(
            name='productitem',
            options={'ordering': ('-id',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
