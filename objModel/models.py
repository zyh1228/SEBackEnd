from os import path
from PIL import Image
from django.db import models

from account.models import User
from utils.utils import upload_obj_cover_dir, upload_obj_model_dir
from seBackEnd.settings import OBJ_MODEL_DIR, OBJ_COVER_DIR


class Category(models.Model):
    category_name = models.CharField(max_length=1024, unique=True, verbose_name='名称')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_edit_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建者')

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'category'
        verbose_name = '模型类别'
        verbose_name_plural = '模型类别'


class ObjModel(models.Model):
    name = models.CharField(max_length=1024, verbose_name='名称')
    description = models.TextField(default='', verbose_name='描述')
    cover = models.ImageField(upload_to=upload_obj_cover_dir, default=path.join('default', 'default.png'), verbose_name='图片')
    file_type = models.CharField(max_length=16, verbose_name='文件类型')
    model_file = models.FileField(upload_to=upload_obj_model_dir, default=path.join('default', 'default.obj'), verbose_name='模型文件')
    file_dir_id = models.CharField(max_length=32, default='default', verbose_name='文件夹id')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_edit_time = models.DateTimeField(auto_now=True, verbose_name='最后编辑时间')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建者')
    visible = models.BooleanField(default=True, verbose_name='是否可见')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.cover:
            return

        super(ObjModel, self).save(force_insert, force_update, using, update_fields)
        image = Image.open(self.cover)
        image = image.resize((600, 400), Image.ANTIALIAS)
        image.save(self.cover.path)

    def get_file_dir(self):
        return path.join(OBJ_MODEL_DIR, self.file_dir_id)

    def get_cover_dir(self):
        return path.join(OBJ_COVER_DIR, self.file_dir_id)

    class Meta:
        db_table = 'obj_model'
        verbose_name = '模型'
        verbose_name_plural = '模型'
