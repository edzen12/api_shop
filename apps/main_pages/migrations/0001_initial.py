# Generated by Django 3.2.5 on 2021-09-01 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0011_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование')),
                ('image', models.ImageField(blank=True, null=True, upload_to='main_page')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Наименование MainPage')),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='categories.category')),
            ],
            options={
                'verbose_name': 'Главная Страница',
                'verbose_name_plural': 'Главные Страницы',
                'ordering': ('-id',),
            },
        ),
    ]
