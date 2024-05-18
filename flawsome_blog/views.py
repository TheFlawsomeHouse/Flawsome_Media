from django.shortcuts import render
from .models import Blog

def blog_Preview(request):
    Blogs = Blog.objects.all() 
    # blogs = Blog.objects.all()
    return render(request, 'blog.html', {'Blogs': Blogs})
    # return render(request, 'blog.html', {'Blog': blogs})

def Blog_details(request):
    id=request.GET.get('id')
    blogs= Blog.objects.filter(id=id)
    return render(request, 'publication.html', {'blogs': blogs})

# def portfolio_view(request):
#     Portfolios = Portfolio.objects.all()
#     return render(request, 'templates/portfolio-1.html', {'Portfolio': Portfolios})