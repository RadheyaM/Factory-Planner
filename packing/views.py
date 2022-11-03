from django.shortcuts import render
from .models import (
    Packaging,
    Product,
    Week,
    Run,
    Packing
)
from django.views.generic import ListView

#________________LIST VIEWS_______________

class PlanView(ListView):
    template_name = 'lists/plan-list.html'
    model = Week