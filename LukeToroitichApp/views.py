from django.shortcuts import render
from django.views.generic import TemplateView 

# Create your views here.

class Home(TemplateView):

    template_name = "index.html"

class hospital(TemplateView):
    template_name = "hospital.html"

# def hospital(request):
#     return render(request, 'hospital.html')