# Generated by Django 3.1.2 on 2020-10-11 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customuser_curent_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='answers',
            field=models.TextField(default='.'),
        ),
    ]
