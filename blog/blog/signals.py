from django.db.models.signals import m2m_changed,post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from pyexpat.errors import messages

from .models import Post

@receiver(m2m_changed,sender=Post.likes.through)
def user_like_changed(sender,instance,**kwargs):
    instance.total_like_count=instance.likes.count()
    instance.save()


@receiver(post_delete, sender=Post)
def user_delete_post(sender, instance, **kwargs):
    author=instance.author
    subject="your post has been deleted"
    message=f"your post has been deleted id({instance.id})"
    send_mail(subject,message,"hszhosalehi81@gmail.com",[author.email],fail_silently=False)
