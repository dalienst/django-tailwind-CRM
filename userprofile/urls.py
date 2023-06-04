from django.urls import path

from userprofile.views import myaccount, SignUpView


app_name = "userprofile"


urlpatterns = [
    path("myaccount/", myaccount, name="myaccount"),
    path("signup/", SignUpView.as_view(), name="signup"),
]