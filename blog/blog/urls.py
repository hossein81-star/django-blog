from django.urls import path
from . import views

app_name="blog"
urlpatterns=[

    path("",views.index,name="index"),
    path("posts-list/<str:category>",views.post_list,name="post_list"),
    path("posts-details/<pk>",views.post_details,name="post_details")

]