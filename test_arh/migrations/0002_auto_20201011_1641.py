# Generated by Django 3.1.2 on 2020-10-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_arh', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Num',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='test_id',
            field=models.IntegerField(default=1),
        ),
    ]
