from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='photos',  blank=True, null=True)
    
    def __str__(self):
        return self.username








