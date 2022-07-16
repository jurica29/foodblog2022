"""Importing models from database"""
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

# Importing models of category and post from blogapp
from blogapp.models import Category, Post

# Sitemap models


class CategorySitemap(Sitemap):
    """Class used for category sitemap"""

    def items(self):
        return Category.objects.all()


class PostSitemap(Sitemap):
    """Class used for post sitemap"""

    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)

    # Last modification date
    def lastmod(self, obj):
        """Function used for last modified date"""
        return obj.created_at
