from django.shortcuts import render
from django.views import View
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'member/index.html')
    
class Services(View):
    def get(self, request):
        return render(request, 'member/services.html')
    
class Portfolio(View):
    def get(self, request):
        return render(request, 'member/portfolio.html')