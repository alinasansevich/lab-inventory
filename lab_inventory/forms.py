#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 13:38:24 2021

@author: alina
"""

from django import forms

from .models import DNA, Primer, Supply, Tissue


class TissueForm(forms.ModelForm):
    class Meta:
        model = Tissue
        fields = ['tissue_info',
                  'date_received',
                  'stored_freezer',
                  'stored_box',
                  ]
        labels = {'Organism / Tissue': '',
                  'Date Received': '',
                  'Freezer / Shelf': '',
                  'Box / Position': '',
                  }


class DNAForm(forms.ModelForm):
    class Meta:
        model = DNA
        fields = ['tissue_info',
                  'extraction_date',
                  'stored_freezer',
                  'stored_box',
                  ]
        labels = {'Organism / Tissue': '',
                  'Extraction Date': '',
                  'Freezer / Shelf': '',
                  'Box / Position': '',
                  }


class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ['product_name',
                  'purchase_order',
                  'date_received',
                  'date_opened',
                  'stored_freezer',
                  ]
        labels = {'Product Name': '',
                  'Purchase Order': '',
                  'Date Received': '',
                  'Date Opened': '',
                  'Freezer / Shelf': '',
                  }


class PrimerForm(forms.ModelForm):
    class Meta:
        model = Primer
        fields = ['primer_name',
                  'primer_seq',
                  'purchase_order',
                  'date_received',
                  'date_opened',
                  'stored_freezer',
                  'stored_box',
                  ]
        labels = {'Primer Name': '',
                  'Primer Sequence': '',
                  'Purchase Order': '',
                  'Date Received': '',
                  'Date Opened': '',
                  'Freezer / Shelf': '',
                  'Box / Position': '',
                  }
