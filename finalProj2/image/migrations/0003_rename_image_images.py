# Generated by Django 4.0 on 2022-03-03 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_remove_image_caption'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Images',
        ),
    ]