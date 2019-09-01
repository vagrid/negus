"""
negus URL Configuration
The 'urlpatterns' list routes URLs to views. 
See: https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy


urlpatterns = [
    path("admin/", admin.site.urls),
]
urlpatterns += i18n_patterns(
    path(gettext_lazy(""), include("navigation.urls", namespace = "navigation")),
    path(gettext_lazy("menu/"), include("menu.urls", namespace = "menu")),
    path(gettext_lazy("contact/"), include("contact.urls", namespace = "contact")), 
    path(gettext_lazy("reservation/"), include("reservation.urls", namespace = "reservation")),
)

