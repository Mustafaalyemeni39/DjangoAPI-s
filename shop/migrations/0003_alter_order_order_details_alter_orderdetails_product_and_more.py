# Generated by Django 4.0.2 on 2022-09-18 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product'),
        ('shop', '0002_order_orderdetails_order_order_details_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_details',
            field=models.ManyToManyField(through='shop.OrderDetails', to='home.Product'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]