from django.shortcuts import render
from .models import (
    Packaging,
    Product,
    Week,
    Run,
    Packing
)
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect

# ______________DASHBAORD______________

def dashboard_index_view(request):
    return render(request, 'dashboard/db-index.html')

def dashboard_teams_view(request):
    return render(request, 'dashboard/db-teams.html')

def dashboard_plans_view(request):
    return render(request, 'dashboard/db-plans.html')

def dashboard_packaging_view(request):
    return render(request, 'dashboard/db-packaging.html')

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
    success_url = '/plan/'

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
    success_url = '/product/'

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
    success_url = '/packaging/'

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
    success_url = '/run/'

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
    success_url = '/packing-run/'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Packing Run Has Been Created'
        )

        return super().form_valid(form)

#_______________UPDATE VIEWS_______________

class UpdatePlanView(UpdateView):
    model = Week
    template_name = 'update/update.html'
    fields = '__all__'
    success_url = '/plan/'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Plan Has Been Updated'
        )

        return super().form_valid(form)


class UpdateProductView(UpdateView):
    model = Product
    template_name = 'update/update.html'
    fields = '__all__'
    success_url = '/product/'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Product Has Been Updated'
        )

        return super().form_valid(form)


class UpdatePackagingView(UpdateView):
    model = Packaging
    template_name = 'update/update.html'
    fields = '__all__'
    success_url = '/packaging/'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Packing Configuration Has Been Updated'
        )

        return super().form_valid(form)


class UpdateRunView(UpdateView):
    model = Run
    template_name = 'update/update.html'
    fields = '__all__'
    success_url = '/run/'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Run Has Been Updated'
        )

        return super().form_valid(form)


class UpdatePackingView(UpdateView):
    model = Packing
    template_name = 'update/update.html'
    fields = '__all__'
    success_url = '/packing-run/'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Packing Run Has Been Updated'
        )

        return super().form_valid(form)


#_______________DELETE VIEWS_______________

class DeletePlanView(DeleteView):
    model = Week
    template_name = 'delete/delete.html'
    fields = '__all__'
    success_url = '/plan/'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Plan Has Been Deleted'
        )

        return super().form_valid(form)


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'delete/delete.html'
    fields = '__all__'
    success_url = '/product/'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Product Has Been Deleted'
        )

        return super().form_valid(form)


class DeletePackagingView(DeleteView):
    model = Packaging
    template_name = 'delete/delete.html'
    fields = '__all__'
    success_url = '/packaging/'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Packing Configuration Has Been Deleted'
        )

        return super().form_valid(form)


class DeleteRunView(DeleteView):
    model = Run
    template_name = 'delete/delete.html'
    fields = '__all__'
    success_url = '/run/'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Run Has Been Deleted'
        )

        return super().form_valid(form)


class DeletePackingView(DeleteView):
    model = Packing
    template_name = 'delete/delete.html'
    fields = '__all__'
    success_url = '/packing-run/'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Packing Run Has Been Deleted'
        )

        return super().form_valid(form)