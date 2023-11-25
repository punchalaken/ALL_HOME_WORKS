from django.db import models
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    image = models.ImageField(verbose_name='Фото', blank=True)
    release_date = models.DateField(verbose_name='Дата выхода')
    lte_exist = models.BooleanField(verbose_name='Поддержка LTE')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")
