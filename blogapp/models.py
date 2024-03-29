"""Importing models from database"""
from ckeditor.fields import RichTextField
from django.db import models


class Category(models.Model):
    """Category model with below fields"""

    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        """Inner class"""

        ordering = ("title",)
        verbose_name_plural = "Categories"

    def __str__(self):
        """Displaying title of the category"""
        return f"{self.title}"

    def get_absolute_url(self):
        """Slug rendering"""
        return f"/{self.slug}/"


class Post(models.Model):
    """Post model"""

    ACTIVE = "active"
    DRAFT = "draft"

    CHOICES_STATUS = ((ACTIVE, "Active"), (DRAFT, "Draft"))

    category = models.ForeignKey(
        Category, related_name="posts", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)

    class Meta:
        """Ordering posts descending by date and time"""

        ordering = ("-created_at",)

    def __str__(self):
        """Displaying post names within django admin area"""
        return f"{self.title}"

    def get_absolute_url(self):
        """Importing models from database"""
        return f"/{self.category.slug}/{self.slug}/"


class Comment(models.Model):
    """Comment model"""

    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Displaying comment creators names within admin area"""
        return f"{self.name}"
