# Generated by Django 2.2.5 on 2019-09-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_book_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
