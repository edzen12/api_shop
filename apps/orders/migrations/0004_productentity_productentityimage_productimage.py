# Generated by Django 3.2.5 on 2021-09-21 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210921_0644'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Наименование товара')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Стоимость')),
                ('size_chart', models.CharField(blank=True, max_length=255, null=True, verbose_name='Размерная сетка')),
                ('size', models.CharField(blank=True, max_length=255, null=True, verbose_name='Размер')),
                ('color', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Цвет')),
                ('order_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='orders.orderentity')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products_order', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_order_image', to='orders.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductEntityImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products_order', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_order_entity_image', to='orders.productentity')),
            ],
        ),
    ]
