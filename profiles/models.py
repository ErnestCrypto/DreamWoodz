from django.db import models
from facialRecognitionSite.models import User

# Create your models here.



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    photo = models.ImageField(blank = True,upload_to = 'photos')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"profile of {self.user.username}"





