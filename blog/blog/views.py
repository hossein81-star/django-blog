from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from  django.contrib.auth import authenticate,login,logout
from taggit.models import Tag
from .forms import *
from django.db.models import Count
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

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
    user=request.user
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
        "category":category,
        "user":user
        }
    return render(request, "blog/post_list.html", context)


def post_details(request,pk):
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    tags=post.tags.all()
    post_tags_ids=post.tags.values_list('id',flat=True)
    similar_post=Post.published.filter(tags__in=post_tags_ids).exclude(id=pk)
    similar_post=similar_post.annotate(same_tags=Count('tags')).order_by("-same_tags","create")[:2]
    return render(request,"blog/post_details.html",{"post":post,"tags":tags,"similar_post":similar_post})

def sign_up(request):
    if request.method == "POST":
        form=RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data["password2"])
            user.save()
            image = form.cleaned_data.get('image')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            if form.cleaned_data["image"]:
                UserImage.objects.create(image_field=image, user=user)
            return redirect("blog:profile")
    else:
        form=RegisterForm()
    return render(request,"forms/sign_up.html",{"form":form})


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
            new_post.author=request.user
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
            post.author = request.user
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

@login_required
@require_POST
def post_like(request):
    post_id=request.POST.get("post_id")
    if post_id is not None:
        post = get_object_or_404(Post, id=post_id)
        user = request.user
        liked = None
        if user in post.likes.all():

            liked=False
            post.likes.remove(user)
        else:
            liked=True
            post.likes.add(user)

        liked_count=post.likes.count()
        response_data={
            "liked":liked,
            "liked_count":liked_count
        }
    else:
        response_data={"error":"post not found"}
    return JsonResponse(response_data)

@login_required
@require_POST
def post_save(request):
    post_id=request.POST.get("post_id")
    if post_id is not None:
        post = get_object_or_404(Post, id=post_id)
        user = request.user
        saved = None
        if user in post.saved_by.all():
            saved=False
            post.saved_by.remove(user)
        else:
            saved=True
            post.saved_by.add(user)


        response_data={
            "saved":saved,

        }
    else:
        response_data={"error":"post not found"}
    return JsonResponse(response_data)