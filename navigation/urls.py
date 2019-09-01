
from django.urls import path
from django.utils.translation import gettext_lazy
from .views import HomePageView, AboutPageView


app_name = "navigation" 


urlpatterns = [
    path("", HomePageView.as_view(), name = "home"),
    path(gettext_lazy("about/"), AboutPageView.as_view(), name ="about"),
]



