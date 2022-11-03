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


class ProductView(ListView):
    template_name = 'lists/product-list.html'
    model = Product


class PackagingView(ListView):
    template_name = 'lists/packaging-list.html'
    model = Packaging


class RunView(ListView):
    template_name = 'lists/run-list.html'
    model = Run


class PackingRunView(ListView):
    template_name = 'lists/packing-run-list.html'
    model = Packing
