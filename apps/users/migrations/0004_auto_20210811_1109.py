# Generated by Django 3.2.5 on 2021-08-11 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210719_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default=1, max_length=255, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default=1, max_length=255, verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='postcode',
            field=models.CharField(default=1, max_length=255, verbose_name='Почтовый индекс'),
            preserve_default=False,
        ),
    ]