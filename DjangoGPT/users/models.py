from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username

class Profile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='_profile_pics')
    # first_registration_date
    # 

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, **kwargs):
        super().save(**kwargs)
        img=Image.open(self.image.path)
        if img.height >500 or img.width>700:
            output_size =(700,500)
            img.thumbnail(output_size)
            img.save(self.image.path)
