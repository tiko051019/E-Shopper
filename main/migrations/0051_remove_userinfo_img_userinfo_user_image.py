# Generated by Django 5.1.6 on 2025-03-29 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_userinfo_adress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='img',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_image',
            field=models.ImageField(null=True, upload_to='Images', verbose_name="User's image"),
        ),
    ]
