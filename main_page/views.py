from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact

# Create your views here.


def index(request):
    return render(request, 'main_page/index.html')


def about(request):
    return render(request, 'main_page/about.html')


def services(request):
    return render(request, 'main_page/services.html')


def contact(request):
    if request.method == 'POST':
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        company = request.POST['company']
        telephone = request.POST['telephone']
        email_address = request.POST['email_address']
        message = request.POST['message']

        # visitors detail information
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR')

        device_type = "Unknown"
        browser_type = "Unknown"
        browser_version = "Unknown"
        os_type = "Unknown"
        os_version = "Unknown"
        if request.user_agent.is_mobile:
            device_type = "Mobile"
        if request.user_agent.is_tablet:
            device_type = "Tablet"
        if request.user_agent.is_pc:
            device_type = "PC"

        browser_type = request.user_agent.browser.family
        browser_version = request.user_agent.browser.version_string
        os_type = request.user_agent.os.family
        os_version = request.user_agent.os.version_string

        contact = Contact(last_name=last_name, first_name=first_name,
                          company=company, telephone=telephone,
                          email_address=email_address, message=message,
                          is_contacted=False, is_contracted=False, is_ok=False,
                          ip_address=ip_address, device_type=device_type,
                          browser_type=browser_type,
                          browser_version=browser_version, os_type=os_type,
                          os_version=os_version)
        contact.save()
        messages.success(
            request, "Your details have been submitted")
    return redirect('/services')
