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

    # class Player(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     slots = models.IntegerField(default=20)
#     progression = models.IntegerField(default=1)
#     nickname = models.CharField(max_length=255)
#     bait = models.ForeignKey(Bait,on_delete=models.DO_NOTHING, null=True)
#     wallet = models.DecimalField(max_digits=10, decimal_places=2, default=40.00)
#     image = models.ImageField(upload_to='player/',width_field=None, max_length=None, default='player/default.jpg')
