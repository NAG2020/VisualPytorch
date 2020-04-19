from django.db import models
# Create your models here.
class Comments(models.Model):
    context = models.TextField()
    title = models.TextField(null=True)
    time = models.DateTimeField(auto_now=True)
    objects =models.Manager()



