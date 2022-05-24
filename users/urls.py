from django.urls import path, reverse_lazy
from django.contrib.auth.views import (LogoutView, PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView,
                                       PasswordChangeView, PasswordChangeDoneView)

from users import views

app_name = "users"

urlpatterns = [
    path("", views.ProfileView.as_view(), name="profile"),

    path("signup/", views.signup, name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy("users:login")), name="logout"),

    path("password_change/", PasswordChangeView.as_view(
        template_name="users/password_change.html"), name="password_change"),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
        name="password_change_done",
    ),

    path("password_reset/", PasswordResetView.as_view(
        template_name="users/password_reset.html",
        email_template_name='users/password_reset_email.html',
        success_url=reverse_lazy('users:password_reset_done')), name="password_reset"),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(template_name="users/reset.html"),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(template_name="users/reset_done.html"),
        name="password_reset_complete",
    ),

    path("skill/<int:pk>/", views.SkillDetailView.as_view(), name="skill_detail"),

    path("<str:user_name>/", views.user_detail, name="detail"),
]
