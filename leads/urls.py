from django.urls import path

from leads import views

app_name = "leads"

urlpatterns = [
    path("", views.LeadsListView.as_view(), name="list"),
    path("add-lead/", views.add_lead, name="add"),
    path("<int:pk>/", views.LeadsDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", views.LeadsDeleteView.as_view(), name="delete"),
    path("<int:pk>/edit/", views.edit_lead, name="edit"),
    path("<int:pk>/convert/", views.convert_to_client, name="convert"),
]
