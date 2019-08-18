
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template


def home_page(request):
    context         = {} 
    template        = "index.html"
    template_object = get_template(template)
    return HttpResponse(template_object.render(context))
