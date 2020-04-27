from django.db import models
# Create your models here.
class Comments(models.Model):
    context = models.TextField(max_length=140)
    title = models.TextField(null=True,max_length=14)
    time = models.DateTimeField(auto_now=True)
    objects =models.Manager()



