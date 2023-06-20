from django.db import models

# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=122)
    address=models.TextField()
    email=models.CharField(max_length=122)
    number=models.CharField(max_length=12)
    tiffin_center=models.CharField(max_length=122)
    
