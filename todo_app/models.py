from django.db import models

# Create your models here.

class todo(models.Model):
    title = models.CharField(max_length=100,default='')
    description = models.TextField(max_length=1000,default='')
    avatar = models.ImageField(upload_to="static/image")
    source = models.CharField(max_length=100,default='')
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title