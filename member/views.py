from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .models import Session
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'member/index.html')
    def post(self, request):
        name = request.POST.get('bookingname')
        number = request.POST.get('number')
        location = request.POST.get('location')
        date = request.POST.get('date')
        service = request.POST.get('service')
        session = Session()
        session.name = name
        session.venue =location
        session.date = date
        session.phone_number = number
        session.service_type = service
        session.save()
        messages.success(request, 'Your request  has been sent successfully')

        return render(request, 'member/index.html')
    
class Services(View):
    def get(self, request):
        return render(request, 'member/services.html')
    def post(self, request):
        name = request.POST.get('bookingname')
        number = request.POST.get('number')
        location = request.POST.get('location')
        date = request.POST.get('date')
        service = request.POST.get('service')
        session = Session()
        session.name = name
        session.venue =location
        session.date = date
        session.phone_number = number
        session.service_type = service
        session.save()
        messages.success(request, 'Your request  has been sent successfully')

        return render(request, 'member/services.html')
    
class Portfolio(View):
    def get(self, request):
        return render(request, 'member/portfolio.html')
    def post(self, request):
        name = request.POST.get('bookingname')
        number = request.POST.get('number')
        location = request.POST.get('location')
        date = request.POST.get('date')
        service = request.POST.get('service')
        session = Session()
        session.name = name
        session.venue =location
        session.date = date
        session.phone_number = number
        session.service_type = service
        session.save()
        messages.success(request, 'Your request  has been sent successfully')

        return render(request, 'member/portfolio.html')