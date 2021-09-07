#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 14:38:03 2021

@author: alina
"""

from django.urls import path
from django.contrib.auth.views import LoginView

# from . import views

app_name = "users"

urlpatterns = [
    # Login page   login is a built-in view, and the dict passes the template to it
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Logout page
    # path('logout/', views.logout_view, name='logout'),
    # Registration page
    # path('register/', views.register, name='register'),  # Remove or Use this line?
    ]