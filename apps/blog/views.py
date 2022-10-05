from django.shortcuts import render
from apps.blog.models import *


def home(request):
    post = Post.objects.filter(estado=True)
    print(post)
    return render(request, 'index.html', {'post': post})