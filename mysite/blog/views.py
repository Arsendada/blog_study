from django.shortcuts import render
from django.http import Http404

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request,
                  'blog/posts/list.html',
                  {'posts': posts})


def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        return Http404('page not found')

    return render(request, 'blog/post/detail.html', {'post': post})