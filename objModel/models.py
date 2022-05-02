from django.db import models
from account.models import User


class Category(models.Model):
    category_name = models.TextField()

    class Meta:
        db_table = 'category'


class ObjModel(models.Model):
    name = models.TextField()
    description = models.TextField(default='')
    cover = models.TextField()
    file_type = models.TextField()
    file = models.TextField()
    model_dir_id = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'obj_model'
