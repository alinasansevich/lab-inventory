"""
Resources:
    https://stackoverflow.com/questions/7287027/displaying-a-table-in-django-from-database/7288237
"""

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import DNA, Primer, Supply, Tissue
from .forms import DNAForm, PrimerForm, SupplyForm, TissueForm


### ### ### base views ### ### ###

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


### ### ### add_new views ### ### ###

def new_tissue(request):
    """Add data about new tissue samples."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TissueForm()
    else:
        # POST data submitted; process data.
        form = TissueForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lab_inventory:tissues'))
    context = {'form': form}
    return render(request, 'lab_inventory/new_tissue.html', context)


def new_dna(request):
    """Add data about new DNA samples."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = DNAForm()
    else:
        # POST data submitted; process data.
        form = DNAForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lab_inventory:dna'))
    context = {'form': form}
    return render(request, 'lab_inventory/new_dna.html', context)


def new_supplies(request):
    """Add data about new lab supplies."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = SupplyForm()
    else:
        # POST data submitted; process data.
        form = SupplyForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lab_inventory:supplies'))
    context = {'form': form}
    return render(request, 'lab_inventory/new_supplies.html', context)


def new_primer(request):
    """Add data about a new PCR primer."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PrimerForm()
    else:
        # POST data submitted; process data.
        form = PrimerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lab_inventory:primer'))
    context = {'form': form}
    return render(request, 'lab_inventory/new_primer.html', context)


### ### ### edit views ### ### ###

def edit_tissue(request, entry_id):
    """Edit an existing entry."""
    
    entry = Tissue.objects.get(id=entry_id)
    
    if request.method != 'POST':
        # Initial request; pre-fillform with the current entry.
        form = TissueForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = TissueForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab_inventory:tissues')
    
    context = {'entry': entry,
                'form': form}
    return render(request, 'lab_inventory/edit_tissue.html', context)


def edit_dna(request, entry_id):
    """Edit an existing DNA entry."""
    
    entry = DNA.objects.get(id=entry_id)
    
    if request.method != 'POST':
        # Initial request; pre-fillform with the current entry.
        form = DNAForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = DNAForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab_inventory:dna')
    
    context = {'entry': entry,
                'form': form}
    return render(request, 'lab_inventory/edit_dna.html', context)


def edit_supplies(request, entry_id):
    """Edit an existing DNA entry."""
    
    entry = Supply.objects.get(id=entry_id)
    
    if request.method != 'POST':
        # Initial request; pre-fillform with the current entry.
        form = SupplyForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = SupplyForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab_inventory:supplies')
    
    context = {'entry': entry,
                'form': form}
    return render(request, 'lab_inventory/edit_supplies.html', context)


def edit_primer(request, entry_id):
    """Edit an existing PCR primer entry."""
    
    entry = Primer.objects.get(id=entry_id)
    
    if request.method != 'POST':
        # Initial request; pre-fillform with the current entry.
        form = PrimerForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = PrimerForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab_inventory:primers')
    
    context = {'entry': entry,
                'form': form}
    return render(request, 'lab_inventory/edit_primer.html', context)

# https://stackoverflow.com/questions/38390177/what-is-a-noreversematch-error-and-how-do-i-fix-it








