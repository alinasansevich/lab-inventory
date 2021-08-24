"""
Resources:
    https://stackoverflow.com/questions/7287027/displaying-a-table-in-django-from-database/7288237
"""

from django.shortcuts import render

from .models import DNA, Primer, Supply, Tissue


def index(request):
    """The home page for lab_inventory."""
    return render(request, 'lab_inventory/index.html')


def tissues(request):
    """Show all tissues' data."""
    tissues = Tissue.objects.all() # get data from db
    context = {'tissues': tissues}
    return render(request, 'lab_inventory/tissues.html', context)


def dna(request):
    """Show data from extracted DNA samples."""
    dna = DNA.objects.all()
    context = {'dna': dna}
    return render(request, 'lab_inventory/dna.html', context)


def supplies(request):
    """Show data from lab supplies."""
    supplies = Supply.objects.all()
    context = {'supplies': supplies}
    return render(request, 'lab_inventory/supplies.html', context)


def primers(request):
    """Show all PCR primers."""
    primers = Primer.objects.all()
    context = {'primers': primers}
    return render(request, 'lab_inventory/primers.html', context)