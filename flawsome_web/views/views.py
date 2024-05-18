from django.shortcuts import render
from flawsome_web.models import Portfolio
def index(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'index.html', {'portfolios': portfolios})

