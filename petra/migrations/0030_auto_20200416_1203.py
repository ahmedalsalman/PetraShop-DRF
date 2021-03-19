# Generated by Django 3.0.5 on 2020-04-16 09:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petra', '0029_auto_20200416_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 12, 3, 9, 959398)),
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='petra.Product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 12, 3, 9, 959398)),
        ),
    ]