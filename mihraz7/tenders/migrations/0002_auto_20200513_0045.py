# Generated by Django 2.2.11 on 2020-05-12 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='tender_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
