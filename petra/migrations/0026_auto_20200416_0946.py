# Generated by Django 3.0.5 on 2020-04-16 06:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petra', '0025_auto_20200415_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 9, 46, 32, 499435)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 9, 46, 32, 499435)),
        ),
    ]
