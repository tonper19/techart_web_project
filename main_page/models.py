from django.db import models
from datetime import datetime


class Contact(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=30, blank=True)
    message = models.TextField(blank=True)
    msg_date = models.DateTimeField(default=datetime.now, blank=True)
    ip_address = models.CharField(max_length=50, blank=True)
    is_contacted = models.BooleanField(default=False, blank=True)
    contact_date = models.DateTimeField(blank=True)
    contact_outcome = models.TextField(blank=True)
    is_contracted = models.BooleanField(default=False, blank=True)
    contract_date = models.DateTimeField(blank=True)
    contract_details = models.TextField(blank=True)
    is_ok = models.BooleanField(blank=True)
    contact_details = models.TextField(blank=True)

    def __str__(self):
        name = f"{self.last_name}, {self.first_name} ({self.company})"
        return name
