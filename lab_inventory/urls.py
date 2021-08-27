#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 11:31:12 2021

@author: alina

Defines URL patterns for lab_inventory.
"""

from django.urls import path
from . import views

# from django.conf import settings
# from django.conf.urls.static import static

app_name = "lab_inventory"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Show all tissues
    path('tissues/', views.tissues, name='tissues'),
    # Show all DNA samples
    path('dna/', views.dna, name='dna'),
    # Show lab supplies
    path('supplies/', views.supplies, name='supplies'),
    # Show PCR primers
    path('primers/', views.primers, name='primers'),
    ]
