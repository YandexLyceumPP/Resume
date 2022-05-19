from django.urls import path

from workshop import views

app_name = "workshop"

urlpatterns = [
    path("", views.workshop, name="workshop"),
    path("field/<pk>/update", views.FieldUpdate.as_view(), name="field_update")
]
