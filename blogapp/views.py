from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from .models import Post, Category

# Create your views here.
def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug, category_slug=category_slug)
    else:
        form = CommentForm()

    return render(request, 'blogapp/detail.html', {'post': post, 'form': form})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    return render(request, 'blogapp/category.html', {'category': category})