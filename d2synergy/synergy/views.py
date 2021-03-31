from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import *


class HomeView(TemplateView):
    template_name = 'synergy/index.html'
