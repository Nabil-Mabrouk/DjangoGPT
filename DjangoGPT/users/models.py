from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    pass

class Profile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='_profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'