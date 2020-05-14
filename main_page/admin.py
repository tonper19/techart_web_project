from django.contrib import admin
from .models import Contact
# Register your models here.
# to create a super user: $ python manage.py createsuperuser
admin.site.register(Contact)
