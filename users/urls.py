from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("", views.profile, name="profile"),
    path("detail/<str:user_name>/", views.user_detail, name="detail"),
]
