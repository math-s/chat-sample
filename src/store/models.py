from django.db import models


class Product(models.Model):
    description = models.TextField()
    url = models.URLField()