# Generated by Django 4.0.4 on 2022-06-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_options_alter_user_avatar_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('0', '未知'), ('1', '男'), ('2', '女')], default='0', max_length=1, verbose_name='性别'),
        ),
    ]
