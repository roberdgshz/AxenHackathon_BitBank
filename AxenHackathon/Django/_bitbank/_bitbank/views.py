from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class ViewHome(TemplateView):
    template_name = '_general/home.html'

class ViewAbout(TemplateView):
    template_name = '_general/about.html'

class ViewLegal(TemplateView):
    template_name = '_general/legal.html'