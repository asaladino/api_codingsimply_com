# Generated by Django 2.2.5 on 2019-09-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20190908_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.CharField(default=None, max_length=256),
        ),
    ]
