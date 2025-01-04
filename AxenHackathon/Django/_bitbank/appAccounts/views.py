from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404

# Create your views here.
class ViewCompletation(TemplateView):
    template_name = 'account/completation.html'

class ViewBase(TemplateView):
    template_name = 'base.html'