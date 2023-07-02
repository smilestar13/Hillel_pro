# Generated by Django 4.2 on 2023-05-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('UAH', 'UAH'), ('USD', 'USD'), ('EUR', 'EUR'), ('BTCUSDT', 'BTC'), ('ETHUSDT', 'ETH')], default='UAH', max_length=16),
        ),
    ]
