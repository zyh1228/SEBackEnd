from os import path
from PIL import Image
from django.db import models

from account.models import User
from utils.utils import upload_dir
from seBackEnd.settings import OBJ_MODEL_DIR


class Category(models.Model):
    category_name = models.CharField(max_length=1024, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_edit_time = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'category'


class ObjModel(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField(default='')
    cover = models.ImageField(upload_to=upload_dir, default=path.join('default', 'default.png'))
    file_type = models.CharField(max_length=16)
    model_file = models.FileField(upload_to=upload_dir, default=path.join('default', 'default.obj'))
    file_dir_id = models.CharField(max_length=32, default='default')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    last_edit_time = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.cover:
            return

        super(ObjModel, self).save(force_insert, force_update, using, update_fields)
        image = Image.open(self.cover)
        image = image.resize((600, 400), Image.ANTIALIAS)
        image.save(self.cover.path)

    def get_file_dir(self):
        return path.join(OBJ_MODEL_DIR, self.file_dir_id)

    class Meta:
        db_table = 'obj_model'
