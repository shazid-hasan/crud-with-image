# Generated by Django 4.2.6 on 2023-10-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_employees_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
