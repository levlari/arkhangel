# Generated by Django 3.1.2 on 2020-10-11 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20201011_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='time_begin',
            field=models.TimeField(default='00:00:00'),
        ),
    ]