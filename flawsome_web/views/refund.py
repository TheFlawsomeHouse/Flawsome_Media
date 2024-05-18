from django.shortcuts import render

def refund(request):
    return render(request, 'refund.html')