from django.shortcuts import render
from .models import (
    Pack,
    Product,
    Week,
    Run,
    PackingRun,
    Team
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import DAYS

# ______________DASHBOARD______________

def dashboard_search_view(request):
    """
    Bring up results based on search value.
    """
    qs = Week.objects.all()
    week_search_query = request.GET.get('search-query')

    if week_search_query != '' and week_search_query is not None:
        qs = qs.filter(name__icontains=week_search_query) 

    context = {
        'queryset': qs,
    }

    return render(request, 'dashboard/db-search.html', context)

def dashboard_teams_view(request):
    """
    a view displaying information about a production week related
    to teams.
    """
    packing_runs = PackingRun.objects.all()
    days = DAYS

    context = {
        'packing_runs': packing_runs,
    }


    return render(request, 'dashboard/db-teams.html', context)

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
    model = Pack


class RunView(ListView):
    template_name = 'lists/run-list.html'
    model = Run


class PackingRunView(ListView):
    template_name = 'lists/packing-run-list.html'
    model = PackingRun

#_______________CREATE VIEWS_______________
class CreatePlanView(CreateView):
    model = Week
    template_name = 'create/create-plan.html'
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
    template_name = 'create/create-product.html'
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
    model = Pack
    template_name = 'create/create-packaging.html'
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
    template_name = 'create/create-run.html'
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
    model = PackingRun
    template_name = 'create/create-packing-run.html'
    fields = '__all__'
    success_url = '/packing-run/'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Packing Run Has Been Created'
        )

        return super().form_valid(form)


#_______________DETAIL VIEWS_______________

class DetailPlanView(DetailView):
    model = Week
    template_name = 'detail/plan-detail.html'
    context_object_name = 'week'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        runs = PackingRun.objects.filter(week__id=self.kwargs['pk'])
        context['runs'] = runs
        return context
    

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
    model = Pack
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
    model = PackingRun
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
    model = Pack
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
    model = PackingRun
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