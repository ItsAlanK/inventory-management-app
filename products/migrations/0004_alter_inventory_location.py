# Generated by Django 3.2 on 2022-06-10 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.location'),
        ),
    ]
