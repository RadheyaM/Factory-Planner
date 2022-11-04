from django.shortcuts import render
from .models import (
    Packaging,
    Product,
    Week,
    Run,
    Packing
)
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.http import HttpResponseRedirect

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

#_______________CREATE VIEWS_______________
class CreatePlanView(CreateView):
    model = Week
    template_name = 'create/create.html'
    fields = '__all__'
    # success_url = HttpResponseRedirect('/plan/')

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Plan Has Been Created'
        )

        return super().form_valid(form)


class CreateProductView(CreateView):
    model = Product
    template_name = 'create/create.html'
    fields = '__all__'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Product Has Been Created'
        )

        return super().form_valid(form)


class CreatePackagingView(CreateView):
    model = Packaging
    template_name = 'create/create.html'
    fields = '__all__'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Packing Configuration Has Been Created'
        )

        return super().form_valid(form)


class CreateRunView(CreateView):
    model = Run
    template_name = 'create/create.html'
    fields = '__all__'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Run Has Been Created'
        )

        return super().form_valid(form)


class CreatePackingView(CreateView):
    model = Packing
    template_name = 'create/create.html'
    fields = '__all__'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Packing Run Has Been Created'
        )

        return super().form_valid(form)