from typing import Any, Optional
from django import http
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from leads.forms import AddLeadForm
from leads.models import Lead
from clients.models import Client
from team.models import Team


class LeadsListView(ListView):
    model = Lead

    @method_decorator(login_required)
    def dispatch(self, *args: Any, **kwargs: Any):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self) -> QuerySet[Any]:
        return Lead.objects.filter(
            created_by=self.request.user, converted_to_client=False
        )


class LeadsDetailView(DetailView):
    model = Lead

    @method_decorator(login_required)
    def dispatch(self, *args: Any, **kwargs: Any):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super(LeadsDetailView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get("pk"))


class LeadsDeleteView(DeleteView):
    model = Lead
    success_url = reverse_lazy("leads:list")

    @method_decorator(login_required)
    def dispatch(self, *args: Any, **kwargs: Any):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super(LeadsDeleteView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get("pk"))

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return self.post(request, *args, **kwargs)



@login_required
def edit_lead(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    if request.method == "POST":
        form = AddLeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()

            messages.success(request, "The changes have been saved")

            return redirect("leads:list")
    else:
        form = AddLeadForm(instance=lead)

    return render(request, "leads/edit_lead.html", {"form": form})


@login_required
def add_lead(request):
    if request.method == "POST":
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            team = Team.objects.filter(created_by=request.user)[0]
            lead.team = team
            lead.save()

            messages.success(request, "The lead was created")

            return redirect("leads:list")
    else:
        form = AddLeadForm()

    return render(request, "leads/add_lead.html", {"form": form})


@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user)[0]

    client = Client.objects.create(
        name=lead.name,
        email=lead.email,
        description=lead.description,
        created_by=request.user,
        team=team,
    )
    lead.converted_to_client = True
    lead.save()

    messages.success(request, "The lead was converted to a client")

    return redirect("leads:list")
