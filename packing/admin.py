from django.contrib import admin
from .models import (
    Pack,
    Product,
    Week,
    Run,
    PackingRun,
    Team)

admin.site.register(Pack)
admin.site.register(Product)
admin.site.register(Week)
admin.site.register(Run)
admin.site.register(PackingRun)
admin.site.register(Team)
