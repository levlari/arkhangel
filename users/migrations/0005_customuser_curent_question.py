# Generated by Django 3.1.1 on 2020-10-06 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='curent_question',
            field=models.IntegerField(default=0),
        ),
    ]
