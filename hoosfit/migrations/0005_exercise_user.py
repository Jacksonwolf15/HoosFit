# Generated by Django 3.1.7 on 2021-03-26 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoosfit', '0004_remove_exercise_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='user',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
