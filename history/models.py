from django.db import models
from account.models import User
from objModel.models import ObjModel


class History(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    obj_model = models.ForeignKey(ObjModel, on_delete=models.CASCADE)
    view_time = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(default=1)

    class Meta:
        db_table = 'history'
        unique_together = ['created_by', 'obj_model']
