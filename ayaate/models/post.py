from django.db import models
from django.utils.text import slugify
from .category import Category
from .subcategory import Subcategory
from .product import Product

class Post(models.Model):
    REACTION_CHOICES = [
        ('good', 'Good'),
        ('very_good', 'Very Good'),
        ('bad', 'Bad'),
        ('too_bad', 'Too Bad'),
    ]

    STATUS_CHOICES = [
        ('publish', 'Publish'),
        ('draft', 'Draft'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/')
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='posts', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='posts', blank=True)
    views = models.PositiveIntegerField(default=0)
    reactions = models.JSONField(default=dict, blank=True)  # Store counts of each reaction type as a JSON field
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        # Initialize reaction counts if empty
        if not self.reactions:
            self.reactions = {'good': 0, 'very_good': 0, 'bad': 0, 'too_bad': 0}
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def update_reaction_count(self, reaction_type):
        """Updates the count of a given reaction type."""
        if reaction_type in self.reactions:
            self.reactions[reaction_type] += 1
            self.save()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Name of the commenter
    body = models.TextField()  # Comment body
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'
