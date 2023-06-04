from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import User

from team.models import Team


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    @transaction.atomic
    def save(self) -> Any:
        user = super().save(commit=False)
        user.save()
        team = Team.objects.create(name=user.username, created_by=user)
        team.members.add(user)
        return user
