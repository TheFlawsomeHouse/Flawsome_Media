from django.shortcuts import render
from flawsome_web.models import Portfolio

def portfolio(request):
    Portfolios = Portfolio.objects.all()
    return render(request, 'portfolio-1.html', {'Portfolios': Portfolios})



def Project(request):
    id=request.GET.get('id')
    Portfolios= Portfolio.objects.filter(id=id)
    return render(request, 'project-1.html', {'Portfolios': Portfolios})

# def portfolio_view(request):
#     Portfolios = Portfolio.objects.all()
#     return render(request, 'templates/portfolio-1.html', {'Portfolio': Portfolios})