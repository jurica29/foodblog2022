"""Importing models from database"""
from ckeditor.fields import RichTextField
from django.db import models

"""Rich text field editor imported for easy editing of posts"""


class Category(models.Model):
    """Importing models from database"""
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        """Inner class"""
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Displays category names within django admin area"""
        return self.title

    def get_absolute_url(self):
        """Importing models from database"""
        return '/%s/' % self.slug


class Post(models.Model):
    """Post model"""
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )

    category = models.ForeignKey(
        Category,
        related_name='posts',
        on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=CHOICES_STATUS,
        default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        """Ordering posts descending by date and time"""
        ordering = ('-created_at',)

    def __str__(self):
        """Displaying post names within django admin area"""
        return self.title

    def get_absolute_url(self):
        """Importing models from database"""
        return '/%s/%s/' % (self.category.slug, self.slug)


class Comment(models.Model):
    """Comment model"""
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Displaying comment creators names within admin area"""
        return self.name
