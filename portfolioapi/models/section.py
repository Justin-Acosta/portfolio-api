from django.db import models
from .wiki import Wiki

class Section(models.Model):
    id = models.AutoField(primary_key=True)
    wiki = models.ForeignKey(Wiki,on_delete=models.CASCADE,null=False)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=64000)
    position = models.IntegerField()
    is_editing = models.BooleanField(default=True)
    image = models.ImageField(upload_to='section/', null=True)
