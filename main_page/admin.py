from django.contrib import admin
from .models import Contact

# 012. Customize Admin Display Data


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'company',
                    'email_address', 'telephone', 'msg_date', 'is_contacted',
                    'is_contracted', 'is_ok', )
    list_display_links = ('id', 'last_name', 'first_name',)
    list_filter = ('company', 'msg_date', )
    list_editable = ('is_contacted', 'is_contracted', 'is_ok', )
    search_fields = ('last_name', 'first_name', 'company', 'email_address',
                     'msg_date', 'is_contacted', )
    list_per_page = 25


# Register your models here.
# to create a super user: $ python manage.py createsuperuser
admin.site.register(Contact, ContactAdmin)
