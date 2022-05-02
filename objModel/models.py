from django.db import models
from account.models import User


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
    cover = models.TextField()  # filepathfield
    file_type = models.CharField(max_length=16)
    file = models.TextField()  # filepathfield
    model_dir_id = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    last_edit_time = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'obj_model'
