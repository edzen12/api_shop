# Generated by Django 3.2.5 on 2021-09-21 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20210921_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productentity',
            name='amount',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
            preserve_default=False,
        ),
    ]
