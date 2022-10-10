from django.db import models


class File(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    file = models.FileField(blank=False, null=False, verbose_name='Расположение')
    remark = models.CharField(max_length=150, blank=True, verbose_name="Примечание")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return self.file.__str__()
