from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *


# Create your views here.


def index(request):
    # load all post give 10 data
    posts = Post.objects.all()[:10];
    cat = Category.objects.all();
    # print(posts)
    data = {
        'posts': posts,
        'cat': cat
    }
    return render(request, 'home.html', data)


def post(request, id):
    post = Post.objects.get(post_id=id)
    print(post)
    return render(request, 'post.html', {'post': post})


def cat(request, title):
    c = Category.objects.get(title=title)
    data = Post.objects.filter(Category__title=title)
    print(data)
    com = {
        'data': data,
        'c': c
    }
    return render(request, 'catagory.html', com)
