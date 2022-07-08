from django.db import models
# Rich text field editor imported for easy editing of posts
from ckeditor.fields import RichTextField

# Describes to database what to store
# Category is one of the main models
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
    
    # Displaying category names within django admin section
    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return '/%s/' % self.slug

# Another model used is "Post"
# Model for post has two possible post statuses
class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

# There are two possible statuses to filter posts
    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )
    
    # These are fields used within admin interface
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

# Ordering posts descending by date and time
    class Meta:
        ordering = ('-created_at',)

# Displaying post names within django admin section
    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)

# Displaying comments
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



