# Generated by Django 4.2.6 on 2023-10-30 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_employees_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='File_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='data')),
            ],
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='img',
            new_name='image',
        ),
    ]
