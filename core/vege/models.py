from django.db import models

# Create your models here.


class Receipe(models.Model):
    id = models.AutoField(),
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(max_length=200)
