from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class MySkill(models.Model):
    skill = models.CharField(max_length=100)
    percent = models.IntegerField()


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    created_date = models.DateTimeField(auto_now_add=True)