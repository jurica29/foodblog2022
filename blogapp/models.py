from django.db import models

# Create your models here.
# Creating post class 
class Post(models.Model):
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


