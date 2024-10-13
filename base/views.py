from django.shortcuts import render
from django.views import View
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, template_name='base/home.html')

class About(View):
    def get(self, request):
        return render(request, template_name='base/story.html')
class Gallery(View):
    def get(self, request):
        return render(request, template_name='base/gallery.html')
class Services(View):
    def get(self, request):
        return render(request, template_name='base/services.html')