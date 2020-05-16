from django.db import models
from datetime import datetime

# once all models are created, run the following:
# $ python manage.py makemigrations
# $ python manage.py migrate
# if changes are made to the models, DO NOT MODIFY THE DB DIRECTLY, use above


class Contact(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100)
    email_address = models.EmailField()
    telephone = models.CharField(max_length=30, blank=True)
    message = models.TextField(blank=True)
    msg_date = models.DateTimeField(default=datetime.now, null=True)
    ip_address = models.CharField(max_length=50, blank=True)
    device_type = models.CharField(max_length=10, blank=True)
    browser_type = models.CharField(max_length=100, blank=True)
    browser_version = models.CharField(max_length=100, blank=True)
    os_type = models.CharField(max_length=100, blank=True)
    os_version = models.CharField(max_length=100, blank=True)
    is_contacted = models.BooleanField(default=False, blank=True)
    contact_date = models.DateTimeField(null=True, blank=True)
    contact_outcome = models.TextField(blank=True)
    is_contracted = models.BooleanField(default=False, blank=True)
    contract_date = models.DateTimeField(null=True, blank=True)
    contract_details = models.TextField(blank=True)
    is_ok = models.BooleanField(blank=True)
    contact_details = models.TextField(blank=True)
    # use DateTimeField(null=True, blank=True) to allow nulls and not required

    def __str__(self):
        name = f"{self.last_name}, {self.first_name} ({self.company})"
        return name
