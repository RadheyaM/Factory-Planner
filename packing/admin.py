from django.contrib import admin
from .models import Packaging, Product, Week, Run, Packing, Teams
# Register your models here.

admin.site.register(Packaging)
admin.site.register(Product)
admin.site.register(Week)
admin.site.register(Run)
admin.site.register(Packing)
admin.site.register(Teams)