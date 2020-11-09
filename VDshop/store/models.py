from django.db import models
from django.urls import reverse

from .utils import generate_slug


class Product(models.Model):

    """ Product implementation """

    title = models.CharField(max_length=150, verbose_name="Наименование")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=5000, null=True, verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение")
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)

