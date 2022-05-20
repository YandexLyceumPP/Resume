from django.urls import path

from workshop import views

app_name = "workshop"

urlpatterns = [
    path("", views.workshop, name="workshop"),

    # Field
    path("field/<pk>/update", views.FieldUpdateView.as_view(), name="field_update"),
    path("field/<pk>/delete", views.FieldDeleteView.as_view(), name="field_delete"),

    # Contact
    path("contact/<pk>/delete", views.ContactDeleteView.as_view(), name="contact_delete"),

    # Resume
    path("resume/<pk>/", views.ResumeDetailView.as_view(), name="resume_detail"),
]
