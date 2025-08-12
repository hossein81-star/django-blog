from django.urls import path,reverse_lazy
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
    path('sign-up/', views.sign_up, name="sign_up"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('password-change/',auth_views.PasswordChangeView.as_view(success_url="done"), name="password-change"),

    path("password-reset/",
         auth_views.PasswordResetView.as_view(success_url=reverse_lazy("blog:password_reset_done")),
         name="password_reset"),
    path('password-change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name="password-change-done"),

    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path(
        "password-reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy("blog:login")),
        name="password_reset_confirm"
    ),
    path("password-reset/complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("post-like/", views.post_like, name="post_like"),
    path("post-save/", views.post_save, name="post_save"),


]

