# Generated by Django 4.2.6 on 2023-10-31 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0009_alter_employees_image_alter_file_data_files'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File_Data',
        ),
        migrations.AlterField(
            model_name='employees',
            name='image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]