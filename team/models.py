from django.contrib.auth.models import User
from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    # max_leads = models.IntegerField()
    # max_client = models.IntegerField()

    # def __str__(self) -> str:
    #     return self.name


class Team(models.Model):
    # plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="teams")
    name = models.CharField(max_length=100, blank=True, null=True)
    members = models.ManyToManyField(User, related_name="teams")
    created_by = models.ForeignKey(
        User, related_name="created_teams", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
