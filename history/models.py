from django.db import models
from account.models import User
from objModel.models import ObjModel


class History(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    obj_model = models.ForeignKey(ObjModel, on_delete=models.CASCADE, verbose_name='模型')
    view_time = models.DateTimeField(auto_now=True, verbose_name='查看时间')
    view_count = models.IntegerField(default=1, verbose_name='次数')

    class Meta:
        db_table = 'history'
        unique_together = ['created_by', 'obj_model']
        verbose_name = '浏览历史'
        verbose_name_plural = '浏览历史'
