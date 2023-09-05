# Generated by Django 4.2.4 on 2023-08-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('short_description', models.TextField(blank=True, verbose_name='Короткое описание')),
                ('long_description', models.TextField(blank=True, verbose_name='Длинное описание')),
                ('coordinate_lng', models.FloatField(verbose_name='Долгота')),
                ('coordinate_lat', models.FloatField(verbose_name='Широта')),
            ],
        ),
    ]
