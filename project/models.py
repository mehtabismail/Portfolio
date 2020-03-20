from django.db import models

# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='image/')
    summary = models.CharField(max_length=250)

    def __str__(self):
        return self.title

