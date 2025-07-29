from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

app_name="blog"
urlpatterns=[

    path("",views.index,name="index"),
    path("posts-list/<str:category>",views.post_list,name="post_list"),
    path("posts-details/<pk>",views.post_details,name="post_details"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', views.user_logout, name="logout"),

]