from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from  django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    return render(request,"blog/index.html")


def post_list(request,category):

    posts = Post.published.filter(category=category)

    context={
        "posts":posts,
        "category":category

    }
    return render(request,"blog/post_list.html",context)

def post_details(request,pk):
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    return render(request,"blog/post_details.html",{"post":post})


def user_logout(request):
    logout(request)
    return redirect("blog:index")