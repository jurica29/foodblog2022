from django.contrib import admin

# Register your models here.
from .models import Post, Category, Comment


# Model for comments
class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

# Model for admin of posts


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}

# Model for admin of categories


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

# Model for admin of comments


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']


# Register models for admin section
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
