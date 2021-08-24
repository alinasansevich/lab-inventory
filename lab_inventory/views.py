from django.shortcuts import render

def index(request):
    """The home page for lab_inventory."""
    return render(request, 'lab_inventory/index.html')

