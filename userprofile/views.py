from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from userprofile.models import Userprofile
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login


from userprofile.forms import SignUpForm

from team.models import Team


# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             user = form.save()
#             Userprofile.objects.create(user=user)
#             team = Team.objects.create(created_by=user)
#             team.members.add(user)
#             team.save()

#             messages.success(request, "Account has been created")

#             return redirect("/login/")
#     else:
#         form = UserCreationForm()

#     return render(request, "userprofile/signup.html", {"form": form})

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'userprofile/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("dashboard:index")



@login_required
def myaccount(request):
    team = Team.objects.filter(created_by=request.user)
    return render(request, "userprofile/myaccount.html", {"team": team})
