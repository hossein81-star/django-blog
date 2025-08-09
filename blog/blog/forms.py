from django import forms
from .models import *
from taggit.forms import TagWidget

class AddPost(forms.ModelForm):
    image = forms.ImageField(label="image", required=True)

    class Meta:

        model=Post
        fields=["title","meta_description","content","category","tags"]


class RegisterForm(forms.ModelForm):
    image = forms.ImageField(label="image", required=False)
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput, label="enter password")
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput, label="repeat password")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "job", "phone"]

    def clean_password2(self):
        cd = self.cleaned_data
        p1 = cd.get("password1")
        p2 = cd.get("password2")
        if p1 != p2:
            raise forms.ValidationError("Passwords do not match. Please make sure both fields are the same.")
        return p2

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError("This phone number is already in use. Please enter a different one.")
        return phone

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose another.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email):
            raise forms.ValidationError("This email is already in use. Please enter a different one.")
        return email
