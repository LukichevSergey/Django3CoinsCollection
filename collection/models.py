from django.db import models
from django.urls import reverse

class Group(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование группы')
    slug = models.SlugField(unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('group', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class Coin(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    title = models.CharField(max_length=255, verbose_name='Наименование монеты')
    slug = models.SlugField(unique=True, verbose_name='URL')
    img = models.ImageField(verbose_name='Фото', upload_to='collection/photo/%Y/%m/%d/')
    year = models.CharField(verbose_name='Год выпуска', max_length=255)
    denomination = models.CharField(max_length=255, verbose_name='Номинал', null=True, blank=True)
    diameter = models.IntegerField(verbose_name='Диаметр',null=True, blank=True)
    edition = models.IntegerField(verbose_name='Тираж', blank=True)
    material = models.CharField(max_length=255, verbose_name='Материал',null=True, blank=True)
    weight = models.DecimalField(verbose_name='Вес',max_digits=9, decimal_places=2,null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Монета'
        verbose_name_plural = 'Монеты'

    def get_absolute_url(self):
        return reverse('coin', kwargs={'slug': self.slug})