from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from accounts.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):

    ACTIVE = 'active'
    DRAFT='Draft'
    CHOICES=(
        (ACTIVE,'incomplete'),(DRAFT,'complete')
        )


    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(unique=True, default='', editable=False)
    description = models.TextField(max_length=255, default="Add a description")
    image = models.ImageField(upload_to='uploads/project_images/', null=True, blank=True)
    video = models.FileField(upload_to='uploads/project_videos/', null=True, blank=True)
    funding_goal = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=False)
    allowed_donors = models.PositiveIntegerField(default=3)
    creator = models.ForeignKey(get_user_model(),related_name="projects", on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name="projects", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 11)])
    status = models.CharField(max_length=20, choices=CHOICES, default='incomplete')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
