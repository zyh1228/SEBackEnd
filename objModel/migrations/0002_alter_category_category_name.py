# Generated by Django 4.0.4 on 2022-05-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.TextField(unique=True),
        ),
    ]
