from django.db import models
from django.contrib.auth.models import User
from .topic import Topic

class Wiki(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    topic = models.ForeignKey(Topic,on_delete=models.DO_NOTHING,null=True)
    title = models.CharField(max_length=255)
    is_draft = models.BooleanField(default=True)
    image = models.ImageField(upload_to='wiki/', null=True)