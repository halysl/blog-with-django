from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Post


def index(request):
    post_list = Post.objects.all().order_by("-created_time")
    return render(request, 'blog/index.html', context={
        'post_list': f'post_list'
    })
