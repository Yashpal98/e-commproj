# Generated by Django 2.2.4 on 2019-09-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190921_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/static/shop/images'),
        ),
    ]
