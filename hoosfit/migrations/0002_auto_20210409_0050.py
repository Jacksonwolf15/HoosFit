# Generated by Django 3.1.7 on 2021-04-09 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoosfit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='playlist',
        ),
        migrations.AddField(
            model_name='exerciseplaylist',
            name='exercises',
            field=models.ManyToManyField(to='hoosfit.Exercise'),
        ),
    ]