from django.db import models


class File(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    file = models.FileField(blank=False, null=False, verbose_name='Расположение')
    remark = models.CharField(max_length=150, blank=True, verbose_name="Примечание")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
