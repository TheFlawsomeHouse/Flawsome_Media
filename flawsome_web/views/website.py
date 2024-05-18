from django.shortcuts import render

def website(request):
    return render(request, 'Website_service.html')