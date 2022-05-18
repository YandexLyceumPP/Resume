from django.urls import path

from users.views import *

app_name = "users"
urlpatterns = [
    path("", ProfileView.as_view(), name="profile"),
    path("settings/", settings, name="settings"),
    path("detail/<str:user_name>/", user_detail, name="detail"),
    path("signup/", signup, name="signup"),
    path("login/", login_page, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),

    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),

    path("<str:user_name>/", user_detail, name="detail"),
]
