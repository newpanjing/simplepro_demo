from django.db import models

# Create your models here.
from simplepro.dialog import ModalDialog


class Dialog(models.Model):
    name = models.CharField(max_length=128, verbose_name='名称', null=True, blank=True)
    description = models.TextField(verbose_name='描述', null=True, blank=True)

    class Meta:
        verbose_name = '对话框'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name
