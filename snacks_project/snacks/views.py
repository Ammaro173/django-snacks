from django.shortcuts import render

# Create your views here.
from tempfile import template

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class AboutView(TemplateView):
    template_name = "about.html"
