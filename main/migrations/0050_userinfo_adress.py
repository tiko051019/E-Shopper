# Generated by Django 5.1.6 on 2025-03-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_payments_history_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='adress',
            field=models.CharField(max_length=255, null=True, verbose_name='Delivery adress'),
        ),
    ]
