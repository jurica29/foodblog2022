# Used for search option
from django.db.models import Q
# Used for rendering, redirecting or displaying 404 page
from django.shortcuts import get_object_or_404, redirect, render

# used to send message
from django.contrib import messages

# Importing comment form as well as post and category field
from .forms import CommentForm
from .models import Post, Category, Comment


def detail(request, category_slug, slug):
    """ Function view used for detail page functionality/display """
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


def deleteComment(request, pk):
    """Function view used for deleting comment"""
    comment = Comment.objects.get(id=pk)

    print(comment)

    if request.method == 'POST':
        comment.delete()

        return redirect('post_detail', comment.post.category.slug, comment.post.slug)

    context = {'item':comment}

    return render(request, 'blogapp/deleteComment.html', context)


def editComment(request, pk):
    """Function view used for editing comment"""
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


def category(request, slug):
    """Function view used for category display/functionality"""
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blogapp/category.html', {'category': category, 'posts': posts})


def search(request):
    """Function view used for search bar functionality/display"""
    query = request.GET.get('query','')

# If query is empty or if it is not aphabetical then warning is displayed.
    if query == "" or not query.isalpha():
        messages.error(request, "Please use one word for your search.")

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query)) 

    return render(request, 'blogapp/search.html', {'posts': posts, 'query': query})
