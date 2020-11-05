from django.db import models

# Create your models here.


class Product(models.Model):

    """ Product implementation """

    name = models.CharField("Name", max_length=150)
    description = models.TextField("Description")
    photo_path = models.CharField("Photo path", max_length=150)  # path to the image of the product
    price = models.IntegerField("Price")
