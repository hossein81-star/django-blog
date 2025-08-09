from django.db import models
from django.utils import timezone

from django.urls import reverse
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):

    date_of_birth = models.DateField(verbose_name="birth_day", blank=True, null=True)
    bio = models.TextField(verbose_name="bio", null=True, blank=True)
    photo = models.ImageField(verbose_name="image", upload_to="account_images/", blank=True, null=True)
    job = models.CharField(max_length=250, verbose_name="job", null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)


class UserImage(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="image")
   image_field = models.ImageField(upload_to="user_image")
   objects = models.Manager()

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
    category=models.CharField(choices= CATEGORY_CHOICES,default="cul")
    status=models.CharField(choices=Status,default="DF",max_length=2)
    author=models.ForeignKey( settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="posts")
    # create=models.DateTimeField(auto_now_add=True)
    # update=models.DateTimeField(auto_now=True)
    # publish=models.DateTimeField(timezone.now)
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    #model manager
    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse("blog:post_details",args=[self.id])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        for img in self.images.all():
            path = img.image_field.path
            storage = img.image_field.storage
            storage.delete(path)
        super().delete(*args, **kwargs)


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
    objects = models.Manager()



