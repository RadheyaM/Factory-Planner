from django.shortcuts import render
from django.db.models import F, Sum
from .models import (
    Packaging,
    Product,
    Week,
    Run,
    Packing
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .utility import get_team_hours, filter_annotate

# ______________DASHBOARD______________

def dashboard_index_view(request):
    return render(request, 'dashboard/db-search.html')

def dashboard_teams_view(request):
    packing = Packing.objects.all()

    t1 = packing.filter(team=1)
    t2 = packing.filter(team=2)
    t3 = packing.filter(team=3)
    t4 = packing.filter(team=4)

    t1_week = get_team_hours(t1)
    t2_week = get_team_hours(t2)
    t3_week = get_team_hours(t3)
    t4_week = get_team_hours(t4)
    t1_total = sum(t1_week)
    t2_total = sum(t2_week)
    t3_total = sum(t3_week)
    t4_total = sum(t4_week)

    context = {
        'packing': packing,
        't1': t1,
        't2': t2,
        't3': t3,
        't4': t4,
        't1_week': t1_week,
        't2_week': t2_week,
        't3_week': t3_week,
        't4_week': t4_week,
        't1_total': t1_total,
        't2_total': t2_total,
        't3_total': t3_total,
        't4_total': t4_total,
        }

    return render(request, 'dashboard/db-teams.html', context)

def dashboard_plans_view(request):
    packing = Packing.objects.all()
    packing_week = packing.filter(week__name='November Wk1')

    sat = packing.filter(day=1, week__name='November Wk1')
    mon = packing.filter(day=2, week__name='November Wk1')
    tue = packing.filter(day=3, week__name='November Wk1')
    wed = packing.filter(day=4, week__name='November Wk1')
    thu = packing.filter(day=5, week__name='November Wk1')
    fri = packing.filter(day=6, week__name='November Wk1')
    

    context = {
        'packing': packing,
        'packing_week': packing_week,
        'sat': sat,
        'mon': mon,
        'tue': tue,
        'wed': wed,
        'thu': thu,
        'fri': fri,
    }


    return render(request, 'dashboard/db-plans.html', context)

def dashboard_packaging_view(request):
    packing = Packing.objects.all()


    sat = packing.filter(day=1, week__name='November Wk1').annotate(inner=Sum(F('name__product__ppc') * F('name__case_qty')), film=Sum((F('name__product__ppc') * F('name__case_qty'))/6000))
    mon = packing.filter(day=2, week__name='November Wk1').annotate(inner=Sum(F('name__product__ppc') * F('name__case_qty')), film=Sum((F('name__product__ppc') * F('name__case_qty'))/6000))
    tue = packing.filter(day=3, week__name='November Wk1').annotate(inner=Sum(F('name__product__ppc') * F('name__case_qty')), film=Sum((F('name__product__ppc') * F('name__case_qty'))/6000))
    wed = packing.filter(day=4, week__name='November Wk1').annotate(inner=Sum(F('name__product__ppc') * F('name__case_qty')), film=Sum((F('name__product__ppc') * F('name__case_qty'))/6000))
    thu = packing.filter(day=5, week__name='November Wk1').annotate(inner=Sum(F('name__product__ppc') * F('name__case_qty')), film=Sum((F('name__product__ppc') * F('name__case_qty'))/6000))
    fri = packing.filter(day=6, week__name='November Wk1').annotate(inner=Sum(F('name__product__ppc') * F('name__case_qty')), film=Sum((F('name__product__ppc') * F('name__case_qty'))/6000))
    


    context = {
        'packing': packing,
        'sat': sat,
        'mon': mon,
        'tue': tue,
        'wed': wed,
        'thu': thu,
        'fri': fri,
    }

    return render(request, 'dashboard/db-packaging.html', context)

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

#_______________DETAIL VIEWS_______________

class DetailPlanView(DetailView):
    model = Week
    template_name = 'detail/plan-detail.html'
    context_object_name = 'week'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        runs = Packing.objects.filter(week__id=self.kwargs['pk'])
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