# Generated by Django 3.0.5 on 2020-05-01 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='_type',
            new_name='type',
        ),
    ]
