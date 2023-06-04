from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from clients.models import Client
from clients.forms import AddClientForm
from team.models import Team


@login_required
def clients_list(request):
    clients = Client.objects.filter(created_by=request.user)
    return render(request, "clients/clients_list.html", {"clients": clients})


@login_required
def clients_details(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    return render(request, "clients/clients_detail.html", {"client": client})


@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    client.delete()

    messages.success(request, "The client was deleted")
    return redirect("clients:list")


@login_required
def edit_client(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)

    if request.method == "POST":
        form = AddClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()

            messages.success(request, "The changes have been saved")

            return redirect("clients:list")
    else:
        form = AddClientForm(instance=client)

    return render(request, "clients/edit_client.html", {"form": form})


@login_required
def add_client(request):
    team = Team.objects.filter(created_by=request.user)
    if request.method == "POST":
        form = AddClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.created_by = request.user
            team = Team.objects.filter(created_by=request.user)[0]
            client.team = team
            client.save()

            messages.success(request, "The client was created")

            return redirect("clients:list")
    else:
        form = AddClientForm()

    return render(request, "clients/add_client.html", {"form": form, "team": team})
