# Generated by Django 4.2.6 on 2023-10-30 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_file_data_alter_employees_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_data',
            name='files',
            field=models.FileField(upload_to='data'),
        ),
    ]
