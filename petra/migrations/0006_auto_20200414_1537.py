# Generated by Django 3.0.5 on 2020-04-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petra', '0005_auto_20200414_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(max_length=150, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, max_length=150, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, max_length=150, null=True, upload_to=''),
        ),
    ]