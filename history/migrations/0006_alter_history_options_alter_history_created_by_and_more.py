# Generated by Django 4.0.4 on 2022-06-20 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objModel', '0006_alter_category_options_alter_objmodel_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('history', '0005_history_view_count_alter_history_view_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name': '浏览历史', 'verbose_name_plural': '浏览历史'},
        ),
        migrations.AlterField(
            model_name='history',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='history',
            name='obj_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objModel.objmodel', verbose_name='模型'),
        ),
        migrations.AlterField(
            model_name='history',
            name='view_count',
            field=models.IntegerField(default=1, verbose_name='次数'),
        ),
        migrations.AlterField(
            model_name='history',
            name='view_time',
            field=models.DateTimeField(auto_now=True, verbose_name='查看时间'),
        ),
    ]
