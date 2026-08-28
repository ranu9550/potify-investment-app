from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("pots/", views.my_pots, name="pots"),
    path("profile/", views.profile, name="profile"),
    path("events/", views.events, name="events"),
]
