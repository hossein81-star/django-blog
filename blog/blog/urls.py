from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

app_name="blog"
urlpatterns=[

    path("",views.index,name="index"),
    path("profile/",views.profile,name="profile"),
    path("posts-list/category/<str:category_slug>",views.post_list,name="post_list"),
    path("posts-list/tag/<slug:tag_slug>/", views.post_list, name="post_list_by_tag"),
    path("posts-details/<pk>",views.post_details,name="post_details"),
    path("add-post", views.add_post, name="add_post"),
    path("posts-delete/<pk>", views.delete_post, name="delete_post"),
    path("posts-edite/<pk>", views.update_post, name="edite_post"),
    path("delete-image/<pk>", views.delete_image, name="delete_image"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', views.user_logout, name="logout"),

]