# Generated by Django 5.1.6 on 2025-03-26 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_remove_items_quantity_usersave_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersave',
            name='line_total',
            field=models.IntegerField(null=True, verbose_name='Line Total'),
        ),
    ]
