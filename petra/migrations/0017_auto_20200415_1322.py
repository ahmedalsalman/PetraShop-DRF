# Generated by Django 3.0.5 on 2020-04-15 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petra', '0016_auto_20200415_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 13, 22, 38, 60146)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 13, 22, 38, 61146)),
        ),
    ]
