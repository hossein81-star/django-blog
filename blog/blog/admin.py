from django.contrib import admin
from .models import *
# Register your models here.
class ImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "auther", "publish", "status"]
    ordering = ["title", "publish"]
    list_filter = ["auther", "publish", "status"]
    search_fields = ["title", "description"]
    raw_id_fields = ["auther"]
    prepopulated_fields = {"slug": ["title"]}
    list_editable = ["status"]
    inlines = [ImageInline]


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [ "title"]