from django import template
from django.urls import resolve, reverse, translate_url, reverse_lazy
from django.utils.translation import activate

register = template.Library()

@register.simple_tag()
def change_lang(request, lang):
	activate(lang)
	return reverse(request.resolver_match.app_name + ":" + request.resolver_match.url_name)

@register.simple_tag()
def active_nav(request, view_url_name):
    url = request.path
    if url == reverse_lazy(view_url_name):
        return "nav-link active"
    return "nav-link"
