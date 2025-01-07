from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class ViewHome(TemplateView):
    template_name = 'general/home.html'