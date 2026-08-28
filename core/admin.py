from django.contrib import admin
from .models import Profile, Pot, Event, Activity

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "kyc_status")
    list_filter = ("kyc_status",)
    search_fields = ("user__username", "user__first_name", "user__last_name", "phone")

@admin.register(Pot)
class PotAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "invested", "expected_gain", "status", "expected_date")
    list_filter = ("status",)
    search_fields = ("name", "user__username")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date", "active")
    list_filter = ("active",)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "amount", "created_at")
