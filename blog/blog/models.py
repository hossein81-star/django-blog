from django.db import models
from django.utils import timezone
from  django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager



# Create your models here.
#Manager
# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(status=Post.Status.PUBLISHED)
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)




class Post(models.Model):
    # category
    CATEGORY_CHOICES = (
        ("Culture", "Culture"),
        ("Business", "Business"),
        ("Lifestyle", "Lifestyle"),
        ("Technology", "Technology"),
    )
    #status
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"
        REJECTED = "RJ", "Rejected"

    title=models.CharField(max_length=250)
    meta_description=models.TextField()
    content = models.TextField(default="no description")
    slug=models.CharField(max_length=250)
    id=models.AutoField(primary_key=True)
    category=models.CharField(choices=CATEGORY_CHOICES,default="cul")
    status=models.CharField(choices=Status,default="DF",max_length=2)
    auther=models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    # create=models.DateTimeField(auto_now_add=True)
    # update=models.DateTimeField(auto_now=True)
    # publish=models.DateTimeField(timezone.now)
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    #model manager
    published=PublishedManager()
    objects=models.Manager()

    def get_absolute_url(self):
        return reverse("blog:post_details",args=[self.id])

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"])
        ]
    def __str__(self):
        return self.title


class PostImage(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="images")
    image_field=models.ImageField(upload_to="post_image")
    # ResizedImageField(size=[2000, 100], crop=['top', 'left'], upload_to='post_image/')

    title = models.CharField(max_length=250,default="image")



