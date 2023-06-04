from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from core.views import index, about

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    
    path(
        "login/",
        views.LoginView.as_view(template_name="userprofile/login.html"),
        name="login",
    ),
    path(
        "logout/",
        views.LogoutView.as_view(),
        name="logout",
    ),
    path("dashboard/", include("dashboard.urls")),
    path("dashboard/", include("userprofile.urls")),
    path("dashboard/leads/", include("leads.urls")),
    path("dashboard/clients/", include("clients.urls")),
    path("dashboard/teams/", include("team.urls")),
    path("admin/", admin.site.urls),
]
