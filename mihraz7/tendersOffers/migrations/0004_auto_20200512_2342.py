# Generated by Django 2.2.11 on 2020-05-12 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendersOffers', '0003_auto_20200512_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenderoffer',
            name='email',
            field=models.EmailField(max_length=60, verbose_name='email'),
        ),
    ]
