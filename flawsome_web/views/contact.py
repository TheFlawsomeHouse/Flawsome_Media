from django.shortcuts import redirect, render
from django.http import HttpResponse
from flawsome_web.models import Contact
from django.contrib import messages
def contact(request):
        return render(request, 'contact.html')
    
def contact_form(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_Number=request.POST.get('phone')
        address=request.POST.get('address')
        services=request.POST.get('services')
        budget=request.POST.get('budget')
        description=request.POST.get('description')
        Contact_Form= Contact(Name=name, Email=email, Mobile_Number=phone_Number, Address=address, Service_Type=services, Budget=budget, Project_Description=description )
        Contact_Form.save()
        messages.success(request, 'Thankyou! Our Representative will cantact you Soon' )
        return redirect("/")
    else:
        return render(request, 'contact.html')