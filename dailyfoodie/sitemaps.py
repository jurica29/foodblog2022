from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

# Importing models of category and post from blogapp
from blogapp.models import Category, Post

# Sitemap models
class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)
    
    def lastmod(self, obj):
        return obj.created_at