# Generated by Django 3.2.5 on 2021-08-29 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='price',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Стоимость'),
        ),
    ]
