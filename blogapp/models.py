from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
    
    # Displaying category names within django admin section
    def __str__(self):
        return self.title 

# Create your models here.
# Creating post class 
class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Ordering posts descending by date and time
    class Meta:
        ordering = ('-created_at',)

# Displaying post names within django admin section
    def __str__(self):
        return self.title 

# Displaying comments
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

