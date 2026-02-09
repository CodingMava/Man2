from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from .utils import check_and_notify_budget
from .models import Transaction
from django.db.models import Sum

def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    totals = Transaction.objects.filter(owner=request.user)\
        .values("currency")\
        .annotate(total=Sum("amount"))
    return render(request, "index.html", {"totals": totals})

def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"]
        )
        login(request, user)
        return redirect("index")
    return render(request, "register.html", {"form": form})
