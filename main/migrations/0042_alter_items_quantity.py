# Generated by Django 5.1.6 on 2025-03-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_items_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='quantity',
            field=models.IntegerField(default=1, null=True, verbose_name='Items number in cart'),
        ),
    ]
