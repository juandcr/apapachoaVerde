# Generated by Django 2.1.3 on 2019-02-12 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_product_paypalbutton'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productId',
            field=models.CharField(default=' ', max_length=10, verbose_name='Clave de producto'),
            preserve_default=False,
        ),
    ]
