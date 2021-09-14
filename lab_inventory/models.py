#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 10:00:26 2021

@author: alina
"""

from django.db import models
from django.core.validators import MinValueValidator

class Tissue(models.Model):
    """Information about tissue samples (tissue type and organism)."""
    
    storage_choices = [
    ('Freezer -20', (
        ('-20/1', "Shelf 1"),
        ('-20/2', "Shelf 2"),
        ('-20/3', "Shelf 3"),
        ('-20/4', "Shelf 4"),
        )),
    ('Freezer -80', (
        ('-80/1', "Shelf 1"),
        ('-80/2', "Shelf 2"),
        ('-80/3', "Shelf 3"),
        ('-80/4', "Shelf 4"),
        )),
    ]    
    tissue_info = models.CharField(max_length=200)
    date_received = models.DateField(auto_now=False)
    date_discarded = models.DateField(auto_now=False, null=True, blank=True)
    stored_freezer = models.CharField(max_length=21, choices=storage_choices)
    stored_box = models.CharField(max_length=9)
    
    def __str__(self):
        """Return a string representation of the model."""
        if len(self.tissue_info) > 50:
            return self.tissue_info[:50] + "..."
        else:
            return self.tissue_info


class DNA(models.Model):
    """Information about DNA extracted from tissue samples (tissue type and organism)."""
    
    storage_choices = [
    ('Freezer -20', (
        ('-20/1', "Shelf 1"),
        ('-20/2', "Shelf 2"),
        ('-20/3', "Shelf 3"),
        ('-20/4', "Shelf 4"),
        )),
    ('Freezer -80', (
        ('-80/1', "Shelf 1"),
        ('-80/2', "Shelf 2"),
        ('-80/3', "Shelf 3"),
        ('-80/4', "Shelf 4"),
        )),
    ]    
    tissue_info = models.ForeignKey(Tissue, on_delete=models.PROTECT)
    extraction_date = models.DateField(auto_now=False)
    date_discarded = models.DateField(auto_now=False, null=True, blank=True)
    stored_freezer = models.CharField(max_length=21, choices=storage_choices)
    stored_box = models.CharField(max_length=9)
    
    class Meta:
        verbose_name_plural = 'DNA'

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.tissue_info)


class Supply(models.Model):
    """Information about lab supplies
    (DNA extraction/purification kits, PCR enzymes & reagents).
    """
    
    storage_choices = [
    ('Freezer -20', (
        ('-20/1', "Shelf 1"),
        ('-20/2', "Shelf 2"),
        ('-20/3', "Shelf 3"),
        ('-20/4', "Shelf 4"),
        )),
    ('Freezer -80', (
        ('-80/1', "Shelf 1"),
        ('-80/2', "Shelf 2"),
        ('-80/3', "Shelf 3"),
        ('-80/4', "Shelf 4"),
        )),
    ]
    product_name = models.CharField(max_length=100)
    purchase_order = models.IntegerField(validators=[MinValueValidator(limit_value=0),])
    date_received = models.DateField(auto_now=False)
    date_opened = models.DateField(auto_now=False, null=True, blank=True)
    date_discarded = models.DateField(auto_now=False, null=True, blank=True)
    stored_freezer = models.CharField(max_length=21, choices=storage_choices)
    
    class Meta:
        verbose_name_plural = 'supplies'
    
    def __str__(self):
        """Return a string representation of the model."""
        if len(self.product_name) > 50:
            return self.product_name[:50] + "..."
        else:
            return self.product_name


class Primer(models.Model):
    """Information about PCR primers."""
    
    storage_choices = [
    ('Freezer -20', (
        ('-20/1', "Shelf 1"),
        ('-20/2', "Shelf 2"),
        ('-20/3', "Shelf 3"),
        ('-20/4', "Shelf 4"),
        )),
    ('Freezer -80', (
        ('-80/1', "Shelf 1"),
        ('-80/2', "Shelf 2"),
        ('-80/3', "Shelf 3"),
        ('-80/4', "Shelf 4"),
        )),
    ]
    primer_name = models.CharField(max_length=30)
    primer_seq = models.CharField(max_length=30)
    purchase_order = models.IntegerField(validators=[MinValueValidator(limit_value=0),])
    date_received = models.DateField(auto_now=False)
    date_opened = models.DateField(auto_now=False, null=True, blank=True)
    date_discarded = models.DateField(auto_now=False, null=True, blank=True)
    stored_freezer = models.CharField(max_length=21, choices=storage_choices)
    stored_box = models.CharField(max_length=9)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.primer_name

