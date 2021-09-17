from django.shortcuts import get_object_or_404, render
from datetime import date
from .models import Post

def get_date(post):
    return post['date']

def starting(req):
    postsData = Post.objects.all().order_by('-date')[:3]
    return render(req, "blog/index.html", {"newests": postsData})

def posts(req):
    postsData = Post.objects.all().order_by('-date')
    return render(req, 'blog/posts.html', {"postsData": postsData})

def post_details(req, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(req, 'blog/post.html', {"post": post})
