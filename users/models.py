from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Cuenta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Perfil'

    def save(self,*args, **kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.imagen.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.imagen.path)


      