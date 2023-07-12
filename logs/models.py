from django.db import models
from profiles.models import Profile
# Create your models here.



class Log(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='logs')
    is_correct = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"log of {self.profile.id}"









