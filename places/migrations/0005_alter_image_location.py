# Generated by Django 4.2.4 on 2023-09-05 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_rename_long_description_place_description_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Локация'),
        ),
    ]
