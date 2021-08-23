from django.contrib import admin

from lab_inventory.models import DNA, Primer, Supply, Tissue

admin.site.register(DNA)
admin.site.register(Primer)
admin.site.register(Supply)
admin.site.register(Tissue)