# Generated by Django 3.2.7 on 2022-04-09 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0006_rename_atogory_image_catogory_catogory_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='Catogory',
            new_name='category',
        ),
    ]
