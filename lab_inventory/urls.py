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
    ]
    # # Show all topics
    # path('topics/', views.topics, name='topics'),
    # # Detail page for a single topic
    # path('<int:topic_id>/', views.topic, name='topic'),
    # # Page for adding a new topic
    # path('new_topic/', views.new_topic, name='new_topic'),
    # # Page for adding a new entry
    # path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # # Page for editing an entry
    # path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # # Add static files
    # ]
