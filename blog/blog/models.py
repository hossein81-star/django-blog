from django.db import models
from django.utils import timezone
from  django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    # category
    CATEGORY_CHOICES = (
        ("cul", "Culture"),
        ("biz", "Business"),
        ("lif", "Lifestyle"),
        ("tec", "Technology"),
    )
    #status
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"
        REJECTED = "RJ", "Rejected"

    title=models.CharField(max_length=250)
    description=models.TextField()
    slug=models.CharField(max_length=250)
    id=models.AutoField(primary_key=True)
    category=models.CharField(choices=CATEGORY_CHOICES,default="cul")
    status=models.CharField(choices=Status,default="DF",max_length=2)
    auther=models.ForeignKey(User,on_delete=models.CASCADE,related_name="auther")
    # create=models.DateTimeField(auto_now_add=True)
    # update=models.DateTimeField(auto_now=True)
    # publish=models.DateTimeField(timezone.now)
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"])
        ]
    def __str__(self):
        return self.title

