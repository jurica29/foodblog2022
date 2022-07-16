"""Importing models from database"""
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


from blogapp.models import Category, Post


class CategorySitemap(Sitemap):
    """Class used for category sitemap"""

    def items(self):
        return Category.objects.all()


class PostSitemap(Sitemap):
    """Class used for post sitemap"""

    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)

    def lastmod(self, obj):
        """Function used for last modified date"""
        return obj.created_at
