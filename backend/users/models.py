from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile', 
        on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    linkedin = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
        



