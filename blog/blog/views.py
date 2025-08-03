from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from  django.contrib.auth import authenticate,login,logout
from taggit.models import Tag

# Create your views here.

def index(request):
    return render(request,"blog/index.html")


# def post_list(request,category=None):
#
#     posts = Post.published.filter(category=category)
#
#
#
#     context={
#         "posts":posts,
#         "category":category,
#
#
#     }
#     return render(request,"blog/post_list.html",context)
#
# def post_list_by_tag(request,tag_slug):
#
#         tag = get_object_or_404(Tag, slug=tag_slug)
#         posts = Post.published.filter(tags__in=[tag])
#
#         context = {
#             "posts": posts,
#         }
#         return render(request, "blog/post_list.html", context)


def post_list(request,category_slug=None,tag_slug=None):
    posts=Post.published.all()
    category=None
    tag=None
    if category_slug:
        category=category_slug
        posts=Post.published.filter(category=category_slug)

    elif tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        posts=Post.published.filter(tags__in=[tag])

    context = {
        "posts": posts,
        "tag":tag,
        "category":category
        }
    return render(request, "blog/post_list.html", context)


def post_details(request,pk):
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    tags=post.tags.all()
    return render(request,"blog/post_details.html",{"post":post,"tags":tags})
def profile(request):
    user=request.user
    posts=request.user.posts.all()
    return render(request, "blog/profile.html", {"user":user,"posts":posts})

def user_logout(request):
    logout(request)
    return redirect("blog:index")
