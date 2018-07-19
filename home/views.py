# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, TemplateView


class HomeView(TemplateView):
    template_name = 'home/home.html'
