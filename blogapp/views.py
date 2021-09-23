from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm


def get_date(post):
    return post['date']


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = 'newests'

    def get_queryset(self):
        set = super().get_queryset()
        data = set[:3]
        return data


class AllPostsView(ListView):
    template_name = 'blog/posts.html'
    model = Post
    ordering = ["-date"]
    context_object_name = 'postsData'


class PostDetailsView(View):
    template_name = 'blog/post.html'

    def get(self, req, slug):
        post = Post.objects.get(slug=slug)
        read_laters = req.session.get('read_laters')
        print(read_laters)
        if read_laters is None:
            read_laters = []
        return render(req, self.template_name, {"post": post, "comment_form": CommentForm, "comments": post.comments.all().order_by("-id"), "read_later": True if post.id in read_laters else False})

    def post(self, req, slug):
        comment_form = CommentForm(req.POST)
        post = Post.objects.get(slug=slug)
        read_laters = req.session.get('read_laters')
        if read_laters is None:
            read_laters = []
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-details", args=[slug]))
        else:
            return render(req, self.template_name, {"post": post, "comment_form": CommentForm, "comments": post.comments.all().order_by("-id"), "read_later": True if post.id in read_laters else False})


class ReadLaterView(View):
    def get(self, req):
        read_laters = req.session.get('read_laters')
        if read_laters is None or len(read_laters) == 0:
            read_laters = []
        else:
            read_laters = Post.objects.filter(id__in=read_laters)
        return render(req, 'blog/read-laters.html', {'read_laters': read_laters})

    def post(self, req, slug):
        read_laters = req.session.get('read_laters')
        if read_laters is None:
            read_laters = []
        id = int(req.POST['post_id'])
        if id not in read_laters:
            read_laters.append(id)
            req.session['read_laters'] = read_laters

        return HttpResponseRedirect(reverse("post-details", args=[slug]))
