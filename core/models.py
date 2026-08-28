from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    KYC_STATUS = [
        ("pending", "Pending"),
        ("verified", "Verified"),
        ("rejected", "Rejected"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    pan = models.CharField(max_length=20, blank=True)
    kyc_status = models.CharField(max_length=20, choices=KYC_STATUS, default="pending")
    avatar = models.URLField(blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Pot(models.Model):
    STATUS = [
        ("in_process", "In Process"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pots")
    name = models.CharField(max_length=120)
    invested = models.DecimalField(max_digits=12, decimal_places=2)
    expected_gain = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS, default="in_process")
    created_at = models.DateTimeField(auto_now_add=True)
    expected_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Event(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField(blank=True)
    event_date = models.DateTimeField()
    join_url = models.URLField(blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["event_date"]

    def __str__(self):
        return self.title

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=160)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
from django.db import models
from django.contrib.auth.models import User


class KYCVerification(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="kyc"
    )

    aadhaar_number = models.CharField(max_length=12)
    pan_number = models.CharField(max_length=10)

    mobile_number = models.CharField(max_length=15)
    father_mobile_number = models.CharField(max_length=15)



    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    rejection_reason = models.TextField(
        blank=True,
        null=True
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    verified_at = models.DateTimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.status}"

