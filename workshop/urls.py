from django.urls import path

from workshop import views

app_name = "workshop"

urlpatterns = [
    # Resume
    path("", views.ResumeCreateView.as_view(), name="resume_create"),
    path("resume/<int:pk>/", views.ResumeDetailView.as_view(), name="resume_detail"),
    path("resume/<int:pk>/update/", views.ResumeUpdateView.as_view(), name="resume_update"),
    path("resume/<int:pk>/delete/", views.ResumeDeleteView.as_view(), name="resume_delete"),

    # Field
    path("field/<int:pk>/update/", views.FieldUpdateView.as_view(), name="field_update"),
    path("field/<int:pk>/delete/", views.FieldDeleteView.as_view(), name="field_delete"),

    # Contact
    path("contact/<int:pk>/delete/", views.ContactDeleteView.as_view(), name="contact_delete"),

    # Block
    path("resume/<int:resume_id>/block/create/", views.BlockCreateView.as_view(), name="block_create"),
    path("resume/<int:resume_id>/block/<int:pk>/update/", views.BlockUpdateView.as_view(), name="block_update"),
    path("block/<int:pk>/delete/", views.BlockDeleteView.as_view(), name="block_delete"),
    path("block/<int:pk>/block_changing_order/<str:direction>/", views.block_changing_order,
         name="block_changing_order"),

    # File
    path("file/<int:pk>/delete/", views.FileDeleteView.as_view(), name="file_delete"),
]
