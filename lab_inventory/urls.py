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
    # Page for adding a new tissue sample
    path('new_tissue/', views.new_tissue, name='new_tissue'),
    # Page for adding a new DNA sample
    path('new_dna/', views.new_dna, name='new_dna'),
    # Page for adding new lab supplies
    path('new_supplies/', views.new_supplies, name='new_supplies'), 
    # Page for adding a new PCR primer
    path('new_primer/', views.new_primer, name='new_primer'), 
    ]











