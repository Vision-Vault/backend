from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

class CustomUser(AbstractUser):

    id = models.AutoField(primary_key=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField()
    email = models.EmailField(unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
