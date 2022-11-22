from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
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

# ______________SEARCH______________

def search_plans(request):
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

    return render(request, 'search/search-plans.html', context)

def search_products(request):
    qs = Product.objects.all()
    product_search_query = request.GET.get('search-query')

    if product_search_query != '' and product_search_query is not None:
        qs = qs.filter(
            Q(name__icontains=product_search_query) |
            Q(customer__icontains=product_search_query)
        ) 

    context = {
        'queryset': qs,
    }
    return render(request, 'search/search-products.html', context)

def search_packaging(request):
    qs = Pack.objects.all()
    pack_search_query = request.GET.get('search-query')

    if pack_search_query != '' and pack_search_query is not None:
        qs = qs.filter(name__icontains=pack_search_query) 

    context = {
        'queryset': qs,
    }
    return render(request, 'search/search-packaging.html', context)

def search_runs(request):
    qs = Run.objects.all()
    run_search_query = request.GET.get('search-query')

    if run_search_query != '' and run_search_query is not None:
        qs = qs.filter(name__icontains=run_search_query) 

    context = {
        'queryset': qs,
    }
    return render(request, 'search/search-runs.html', context)


#_______________CREATE VIEWS_______________
class CreatePlanView(CreateView):
    model = Week
    template_name = 'create/create-plan.html'
    fields = '__all__'
    success_url = reverse_lazy('search-plans')

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
    success_url = reverse_lazy('search-products')

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
    success_url = reverse_lazy('search-packaging')

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
    success_url = reverse_lazy('search-runs')

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
    success_url = reverse_lazy('search-plans')

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        runs = PackingRun.objects.filter(week__id=pk).get_calc_trays()
        team_times = PackingRun.objects.get_team_times(pk)
        team_day_times = PackingRun.objects.get_team_day_times(pk)
        context = {
            'runs': runs,
            'tt': team_times,
            'tdt': team_day_times,
        }
        return context
    

#_______________UPDATE VIEWS_______________

class UpdatePlanView(UpdateView):
    model = Week
    template_name = 'update/update.html'
    fields = '__all__'
    success_url = reverse_lazy('search-plans')

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
    success_url = reverse_lazy('search-products')

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
    success_url = reverse_lazy('search-packaging')

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
    success_url = reverse_lazy('search-runs')

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
    success_url = reverse_lazy('search-plans')

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
    success_url = reverse_lazy('search-plans')

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
    success_url = reverse_lazy('search-products')

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
    success_url = reverse_lazy('search-packaging')

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
    success_url = reverse_lazy('search-runs')

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
    success_url = reverse_lazy('search-plans')

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Packing Run Has Been Deleted'
        )

        return super().form_valid(form)