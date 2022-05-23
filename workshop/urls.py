from django.urls import path

from workshop import views

app_name = "workshop"

urlpatterns = [
    # path("", views.workshop, name="workshop"),
    # Resume
    path("resume/create", views.ResumeCreateView.as_view(), name="resume_create"),
    path("resume/<int:pk>/", views.ResumeDetailView.as_view(), name="resume_detail"),
    path("resume/<int:pk>/update/", views.ResumeUpdateView.as_view(), name="resume_update"),
    path("resume/<int:pk>/delete/", views.ResumeDeleteView.as_view(), name="resume_delete"),

    # Field
    path("field/<int:pk>/update/", views.FieldUpdateView.as_view(), name="field_update"),
    path("field/<int:pk>/delete/", views.FieldDeleteView.as_view(), name="field_delete"),

    # Contact
    path("contact/<int:pk>/delete/", views.ContactDeleteView.as_view(), name="contact_delete"),
]
