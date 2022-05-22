from django.urls import path

from workshop import views

app_name = "workshop"

urlpatterns = [
    # Resume
    path("", views.resume_create, name="workshop"),
    path("resume/<int:pk>/", views.ResumeDetailView.as_view(), name="resume_detail"),
    path("resume/<int:pk>/update/", views.resume_update, name="resume_detail"),

    # Field
    path("field/<int:pk>/update/", views.FieldUpdateView.as_view(), name="field_update"),
    path("field/<int:pk>/delete/", views.FieldDeleteView.as_view(), name="field_delete"),

    # Contact
    path("contact/<int:pk>/delete/", views.ContactDeleteView.as_view(), name="contact_delete"),
]
