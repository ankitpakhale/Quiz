# Generated by Django 3.0 on 2022-04-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20220403_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerform',
            name='marks',
        ),
        migrations.AddField(
            model_name='signupform',
            name='marks',
            field=models.FloatField(default=0.0),
        ),
    ]
