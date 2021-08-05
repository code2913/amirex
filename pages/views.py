from django.shortcuts import render
from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = "pages/index.html"


class Contact(TemplateView):
    template_name = "pages/contact.html"
