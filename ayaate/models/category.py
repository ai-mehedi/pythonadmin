from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    TOPIC_CHOICES = [
        ('post', 'Post'),
        ('video', 'Video'),
        ('product', 'Product'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    mehedi = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
