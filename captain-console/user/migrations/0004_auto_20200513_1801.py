# Generated by Django 3.0.6 on 2020-05-13 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200512_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
