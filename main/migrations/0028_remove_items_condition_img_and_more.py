# Generated by Django 5.1.6 on 2025-03-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_items_condition_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='condition_img',
        ),
        migrations.AddField(
            model_name='itemsdetails',
            name='condition_img',
            field=models.ImageField(null=True, upload_to='Images', verbose_name='Logo <New>'),
        ),
    ]
