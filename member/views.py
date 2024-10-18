from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Session, Message
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

def send_messages(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        new_message = Message()
        new_message.name = name
        new_message.email = email
        new_message.message = message
        new_message.save()
        messages.success(request,  f'Thank you {name}, Your message has been sent successfully')

        return redirect('home')
    else:
        return render(request, 'member/index.html')
    