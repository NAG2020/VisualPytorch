from django.db import models
# Create your models here.
class Inference(models.Model):
    pic = models.TextField(max_length=140,default="error.jpg")
    objects =models.Manager()



