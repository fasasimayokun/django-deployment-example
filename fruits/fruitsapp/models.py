from django.db import models

# Create your models here.

class MyFruit(models.Model):

    image = models.ImageField(null=True, blank=True, upload_to="images/")
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=120)
    description = models.TextField(max_length=256)

    def __str__(self):
        return self.name