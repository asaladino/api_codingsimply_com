# Generated by Django 2.2.5 on 2019-09-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20190908_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to='uploads/books/'),
        ),
    ]
