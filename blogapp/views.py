# Used for search option
from django.db.models import Q
# Used for rendering, redirecting or displaying 404 page
from django.shortcuts import get_object_or_404, redirect, render

# used to send message
from django.contrib import messages

# Importing comment form as well as post and category field
from .forms import CommentForm
from .models import Post, Category, Comment

# Function view used for detail page functionality/display
def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.name = request.user.username
            comment.save()

            return redirect('post_detail', slug=slug, category_slug=category_slug)
    else:
        form = CommentForm()

    return render(request, 'blogapp/detail.html', {'post': post, 'form': form})

# Function view used for deleting comment
def deleteComment(request, pk):

    comment = Comment.objects.get(id=pk)

    print(comment)

    if request.method == 'POST':
        comment.delete()

        return redirect('post_detail', comment.post.category.slug, comment.post.slug)

    context = {'item':comment}

    return render(request, 'blogapp/deleteComment.html', context)

# Function view used for editing comment
def editComment(request, pk):

    comment = Comment.objects.get(id=pk)
    form = CommentForm(instance=comment)

    # print(comment)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()

        return redirect('post_detail', comment.post.category.slug, comment.post.slug)

    context = {'form':form, 'comment': comment}

    return render(request, 'blogapp/editComment.html', context)

# Function view used for category display/functionality
def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blogapp/category.html', {'category': category, 'posts': posts})

# Function view used for search bar functionality/display
def search(request):
    query = request.GET.get('query','')

# If query is empty or if it is not aphabetical then warning is displayed.
    if query == "" or not query.isalpha():
        messages.error(request, "Hey! Please use valid input!")

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query)) 

    return render(request, 'blogapp/search.html', {'posts': posts, 'query': query})
