# Generated by Django 5.1.6 on 2025-03-09 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_category_sub_bool'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='sub_bool',
            field=models.BooleanField(default=True, null=True, verbose_name='Has sub. or not'),
        ),
    ]
