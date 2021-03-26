# Generated by Django 3.1.7 on 2021-03-23 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hoosfit', '0002_exercise_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to=settings.AUTH_USER_MODEL),
        ),
    ]