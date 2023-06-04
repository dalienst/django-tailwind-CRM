from django.urls import path

from clients import views

app_name = "clients"

urlpatterns = [
    path("", views.clients_list, name="list"),
    path("<int:pk>/", views.clients_details, name="detail"),
    path("add-client/", views.add_client, name="add"),
    path("<int:pk>/delete/", views.client_delete, name="delete"),
    path("<int:pk>/edit/", views.edit_client, name="edit"),
]
