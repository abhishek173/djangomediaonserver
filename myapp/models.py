from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to='pimages',blank=True)
    rdoc = models.FileField(upload_to='rdocs',blank=True)
    