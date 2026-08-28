from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect
from .models import Profile, Pot, Event, Activity

@login_required
def dashboard(request):
    pots = Pot.objects.filter(user=request.user)
    total_invested = pots.aggregate(v=Sum("invested"))["v"] or Decimal("0")
    total_gained = pots.filter(status="completed").aggregate(v=Sum("expected_gain"))["v"] or Decimal("0")
    upcoming_gain = pots.filter(status="in_process").aggregate(v=Sum("expected_gain"))["v"] or Decimal("0")

    context = {
        "total_invested": total_invested,
        "total_gained": total_gained,
        "upcoming_gain": upcoming_gain,
        "pots_in_process": pots.filter(status="in_process").count(),
        "pots_completed": pots.filter(status="completed").count(),
        "pots_canceled": pots.filter(status="canceled").count(),
        "pots": pots.order_by("-created_at")[:5],
        "events": Event.objects.filter(active=True).order_by("event_date")[:4],
        "activities": Activity.objects.filter(user=request.user)[:5],
    }
    return render(request, "dashboard.html", context)

@login_required
def my_pots(request):
    status = request.GET.get("status")
    pots = Pot.objects.filter(user=request.user)
    if status in {"in_process", "completed", "canceled"}:
        pots = pots.filter(status=status)
    context = {
        "pots": pots.order_by("-created_at"),
        "selected": status or "all",
    }
    return render(request, "pots.html", context)

@login_required
def profile(request):
    profile_obj, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        request.user.first_name = request.POST.get("first_name", "")
        request.user.last_name = request.POST.get("last_name", "")
        request.user.email = request.POST.get("email", "")
        request.user.save()
        profile_obj.phone = request.POST.get("phone", "")
        profile_obj.address = request.POST.get("address", "")
        profile_obj.save()
        return redirect("profile")
    return render(request, "profile.html", {"profile": profile_obj})

@login_required
def events(request):
    return render(request, "events.html", {
        "events": Event.objects.filter(active=True).order_by("event_date")
    })
