from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length = 100)
    last_watered = models.DateTimeField('last_watered')
