from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from  django.contrib.auth import authenticate,login,logout
from taggit.models import Tag
from .forms import *

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

def add_post(request):
    category = Post.CATEGORY_CHOICES
    if request.method=='POST':
        form=AddPost(request.POST,request.FILES)

        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.auther=request.user
            new_post.save()
            form.save_m2m()
            image = form.cleaned_data.get('image')
            if image:
                PostImage.objects.create(image_field=image, post=new_post)

            return redirect("blog:profile")
    else:
        form = AddPost()
    return render(request,"forms/add_post.html",{"form":form,"category":category})


def delete_post(request, pk):
    post=get_object_or_404(Post, id=pk)
    if request.method=="POST":
        post.delete()
        return redirect("blog:profile")

    return render(request,"forms/del_post.html",{"post":post})


def update_post(request, pk):
    post=get_object_or_404(Post, id=pk)
    post_tag=tags_text = ", ".join(tag.name for tag in post.tags.all())

    category = Post.CATEGORY_CHOICES
    if request.method == "POST":
        form = AddPost(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.auther = request.user
            post.save()
            form.save_m2m()
            image = form.cleaned_data.get('image')
            if image:
                PostImage.objects.create(image_field=image, post=post)

            return redirect("blog:profile")
    else:
        form = AddPost(instance=post)

    context = {
        'form': form,
        "post":post,
        "category":category,
        "post_tag":post_tag
    }

    return render(request, "forms/add_post.html", context)

def delete_image(request, pk):
    image = get_object_or_404(PostImage, id=pk)
    image.delete()
    return redirect("blog:add_post")