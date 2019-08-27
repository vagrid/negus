from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "navigation/index.html"

class AboutPageView(TemplateView):
    template_name = "navigation/about.html"

"""
def home_page(request):
    context         = {} 
    template        = "index.html"
    template_object = get_template(template)
    return HttpResponse(template_object.render(context))
"""
