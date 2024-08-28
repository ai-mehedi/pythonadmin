from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from .category import Category
from .subcategory import Subcategory
from tinymce.models import HTMLField

class Video(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    url = models.URLField()
    keyword = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='videos', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='videos', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
