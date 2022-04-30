from django.shortcuts import render
from .models import Portfolio

# Create your views here.
def portfolios(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio/portfolio.html', {'portfolios':portfolios})