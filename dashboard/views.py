from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from leads.models import Lead
from clients.models import Client
from team.models import Team


@login_required
def dashboard(request):
    team = Team.objects.filter(created_by=request.user)
    leads = Lead.objects.filter(
        created_by=request.user, converted_to_client=False
    ).order_by("-created_at")[0:5]
    clients = Client.objects.filter(created_by=request.user).order_by("-created_at")[
        0:5
    ]

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "leads": leads,
            "clients": clients,
        },
    )
