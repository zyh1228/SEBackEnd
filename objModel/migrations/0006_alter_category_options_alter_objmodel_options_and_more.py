# Generated by Django 4.0.4 on 2022-05-04 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('objModel', '0005_objmodel_visible_alter_objmodel_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '模型类别', 'verbose_name_plural': '模型类别'},
        ),
        migrations.AlterModelOptions(
            name='objmodel',
            options={'verbose_name': '模型', 'verbose_name_plural': '模型'},
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=1024, unique=True, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='category',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
        migrations.AlterField(
            model_name='category',
            name='last_edit_time',
            field=models.DateTimeField(auto_now=True, verbose_name='最后修改时间'),
        ),
        migrations.AlterField(
            model_name='objmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objModel.category', verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='objmodel',
            name='cover',
            field=models.ImageField(default='default\\default.png', upload_to=utils.utils.upload_obj_cover_dir, verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='objmodel',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='objmodel',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
        migrations.AlterField(
            model_name='objmodel',
            name='description',
            field=models.TextField(default='', verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='objmodel',
            name='file_dir_id',
            field=models.CharField(default='default', max_length=32, verbose_name='文件夹id'),
        ),
        migrations.AlterField(
            model_name='objmodel',
            name='file_type',
            field=models.CharField(max_length=16, verbose_name='文件类型'),
        ),
        migrations.AlterField(
            model_name='objmodel',
            name='last_edit_time',
            field=models.DateTimeField(auto_now=True, verbose_name='最后编辑时间'),
        ),
        migrations.AlterField(
            model_name='objmodel',
            name='model_file',
            field=models.FileField(default='default\\default.obj', upload_to=utils.utils.upload_obj_model_dir, verbose_name='模型文件'),
        ),
        migrations.AlterField(
            model_name='objmodel',
            name='name',
            field=models.CharField(max_length=1024, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='objmodel',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='是否可见'),
        ),
    ]