# Generated by Django 3.0.5 on 2020-04-16 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petra', '0033_auto_20200416_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 12, 14, 11, 637257)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 12, 14, 11, 638257)),
        ),
    ]