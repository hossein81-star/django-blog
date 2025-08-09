from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
class ImageInline(admin.TabularInline):
    model = PostImage
    extra = 1
class UserImageInline(admin.TabularInline):
    model = UserImage
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "publish", "status"]
    ordering = ["title", "publish"]
    list_filter = ["author", "publish", "status"]
    search_fields = ["title", "description"]
    raw_id_fields = ["author"]
    prepopulated_fields = {"slug": ["title"]}
    list_editable = ["status"]
    inlines = [ImageInline]


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [ "title"]



@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "email", "last_name", "job", "phone"]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {"fields": ("date_of_birth", "phone", "job", "bio")}),)
    inlines = [UserImageInline]

