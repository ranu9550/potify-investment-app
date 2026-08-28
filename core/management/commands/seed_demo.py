from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from core.models import Profile, Pot, Event, Activity

class Command(BaseCommand):
    help = "Create demo user and sample data"

    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(username="abhiram")
        if created:
            user.set_password("demo12345")
            user.first_name = "Abhiram"
            user.last_name = "Baddam"
            user.email = "abhiram@example.com"
            user.save()

        Profile.objects.update_or_create(
            user=user,
            defaults={"phone":"+91 97000 00000", "kyc_status":"verified"}
        )

        Pot.objects.filter(user=user).delete()
        Pot.objects.bulk_create([
            Pot(user=user,name="Bluechip Fund SIP",invested=50000,expected_gain=5000,status="in_process"),
            Pot(user=user,name="Tax Saving Fund",invested=100000,expected_gain=8500,status="in_process"),
            Pot(user=user,name="Index Fund",invested=75000,expected_gain=3200,status="in_process"),
            Pot(user=user,name="Balanced Growth Fund",invested=20000,expected_gain=2000,status="completed"),
            Pot(user=user,name="Old SIP",invested=15000,expected_gain=1200,status="canceled"),
        ])

        Event.objects.all().delete()
        now = timezone.now()
        Event.objects.bulk_create([
            Event(title="Wealth Building Webinar",description="Learn investment basics and long-term wealth building.",event_date=now+timedelta(days=2),join_url="https://example.com"),
            Event(title="Market Outlook",description="Monthly market discussion.",event_date=now+timedelta(days=7),join_url="https://example.com"),
        ])

        Activity.objects.filter(user=user).delete()
        Activity.objects.bulk_create([
            Activity(user=user,title="SIP Investment in Bluechip Fund",amount=5000),
            Activity(user=user,title="Tax Saving Investment",amount=10000),
            Activity(user=user,title="SIP Investment in Index Fund",amount=3000),
        ])

        self.stdout.write(self.style.SUCCESS("Demo data created. Login: abhiram / demo12345"))
