# Generated by Django 3.2 on 2021-04-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoosfit', '0004_auto_20210412_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='previous_login',
            field=models.DateTimeField(null=True, verbose_name='streak'),
        ),
    ]
