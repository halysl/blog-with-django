import re
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Post
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
import markdown


def index(request):
    post_list = Post.objects.all().order_by("-created_time")
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md_obj = markdown.Markdown(extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      TocExtension(slugify=slugify),
                                  ])
    post.body = md_obj.convert(post.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md_obj.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, "blog/detail.html", context={"post": post})
