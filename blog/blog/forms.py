from django import forms
from .models import *
from taggit.forms import TagWidget

class AddPost(forms.ModelForm):
    image = forms.ImageField(label="image", required=False)

    class Meta:

        model=Post
        fields=["title","meta_description","content","category","tags"]
