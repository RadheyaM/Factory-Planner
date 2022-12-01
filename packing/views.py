from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from .models import Pack, Product, Week, Run, PackingRun, Team
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import DAYS
from .forms import PackingRunForm

# ______________SEARCH______________


def search_plans(request):
    """
    This view is the search nexus for all Week Plans.
    In this view plans show up as cards below the search bar
    and CRUD functionality is made available to the user.
    """
    qs = Week.objects.all()
    week_search_query = request.GET.get("search-query")

    if week_search_query != "" and week_search_query is not None:
        qs = qs.filter(name__icontains=week_search_query)

    context = {
        "queryset": qs,
    }

    return render(request, "search/search-plans.html", context)


def search_products(request):
    """
    This view is the search nexus for all Products.
    In this view Products show up as cards below the search bar
    and CRUD functionality is made available to the user.
    """
    qs = Product.objects.all()
    product_search_query = request.GET.get("search-query")

    if product_search_query != "" and product_search_query is not None:
        qs = qs.filter(
            Q(name__icontains=product_search_query)
            | Q(customer__icontains=product_search_query)
        )

    context = {
        "queryset": qs,
    }
    return render(request, "search/search-products.html", context)


def search_packaging(request):
    """
    This view is the search nexus for all Packaging Configurations.
    In this view Packing Configs show up as cards below the search bar
    and CRUD functionality is made available to the user.
    """
    qs = Pack.objects.all()
    pack_search_query = request.GET.get("search-query")

    if pack_search_query != "" and pack_search_query is not None:
        qs = qs.filter(name__icontains=pack_search_query)

    context = {
        "queryset": qs,
    }
    return render(request, "search/search-packaging.html", context)


def search_runs(request):
    """
    This view is the search nexus for all Runs.
    In this view Runs show up as cards below the search bar
    and CRUD functionality is made available to the user.
    """
    qs = Run.objects.all()
    run_search_query = request.GET.get("search-query")

    if run_search_query != "" and run_search_query is not None:
        qs = qs.filter(name__icontains=run_search_query)

    context = {
        "queryset": qs,
    }
    return render(request, "search/search-runs.html", context)


# _______________CREATE VIEWS_______________
class CreatePlanView(PermissionRequiredMixin, CreateView):
    """
    View to create a Week Plan.
    """
    permission_required = "packing.create_week"
    model = Week
    template_name = "create/create-plan.html"
    fields = "__all__"
    success_url = reverse_lazy("search-plans")

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS, "The Plan Has Been Created"
        )

        return super().form_valid(form)


class CreateProductView(PermissionRequiredMixin, CreateView):
    """
    View to create a Product.
    """
    permission_required = "packing.create_product"
    model = Product
    template_name = "create/create-product.html"
    fields = "__all__"
    success_url = reverse_lazy("search-products")

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS, "The Product Has Been Created"
        )

        return super().form_valid(form)


class CreatePackagingView(PermissionRequiredMixin, CreateView):
    """
    View to create a Packing Configuration.
    """
    permission_required = "packing.create_packaging"
    model = Pack
    template_name = "create/create-packaging.html"
    fields = "__all__"
    success_url = reverse_lazy("search-packaging")

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS,
            "The Packing Configuration Has Been Created"
        )

        return super().form_valid(form)


class CreateRunView(PermissionRequiredMixin, CreateView):
    """
    View to create a Run
    """
    permission_required = "packing.create_run"
    model = Run
    template_name = "create/create-run.html"
    fields = "__all__"
    success_url = reverse_lazy("search-runs")

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS,
            "The Run Has Been Created")

        return super().form_valid(form)


class CreatePackingView(PermissionRequiredMixin, CreateView):
    """
    View to assign a Packing Run to a Week Plan.
    """
    permission_required = "packing.create_packingrun"
    model = PackingRun
    fields = ['name', 'week', 'team', 'day', 'time', 'notes',]
    template_name = "create/create-packing-run.html"

    # week automatically selected when create form loaded.
    def get_initial(self):
        initial = super(CreatePackingView, self).get_initial()
        initial['week'] = Week.objects.get(pk=self.kwargs['pk'])
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["week"] = Week.objects.get(pk=self.kwargs['pk'])
        return context
    
    # redirect to original plan detail page.
    def get_success_url(self):
        return reverse('plan-detail', kwargs={'pk' : self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.add_message(
            self.request, messages.SUCCESS, "The Packing Run Has Been Created"
        )

        return super().form_valid(form)


# _______________DETAIL VIEWS_______________


class DetailPlanView(DetailView):
    """
    This view is the main dashboard view for a week plan.
    It contains report tables with relevant information for
    staff directly involved in the packing process.
    """
    model = Week
    template_name = "detail/plan-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        week = Week.objects.get(id=pk)
        runs = PackingRun.objects.filter(week__id=pk).get_calc_trays()
        notes = PackingRun.objects.filter(week__id=pk).exclude(notes__isnull=True)
        team_times = PackingRun.objects.get_team_times(pk)
        team_day_times = PackingRun.objects.get_team_day_times(pk)
        context = {
            "runs": runs,
            "tt": team_times,
            "tdt": team_day_times,
            "week": week,
            "notes": notes,
        }
        return context


# _______________UPDATE VIEWS_______________


class UpdatePlanView(PermissionRequiredMixin, UpdateView):
    """
    View to Edit a Week Plan.
    """
    permission_required = "packing.edit_week"
    model = Week
    template_name = "update/update-plan.html"
    fields = "__all__"
    success_url = reverse_lazy("search-plans")

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS, "The Plan Has Been Updated"
        )

        return super().form_valid(form)


class UpdateProductView(PermissionRequiredMixin, UpdateView):
    """
    View to Edit a Product.
    """
    permission_required = "packing.edit_product"
    model = Product
    template_name = "update/update-product.html"
    fields = "__all__"
    success_url = reverse_lazy("search-products")

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS, "The Product Has Been Updated"
        )

        return super().form_valid(form)


class UpdatePackagingView(PermissionRequiredMixin, UpdateView):
    """
    View to Edit a Packaging Configuration.
    """
    permission_required = "packing.edit_packaging"
    model = Pack
    template_name = "update/update-packaging.html"
    fields = "__all__"
    success_url = reverse_lazy("search-packaging")

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS,
            "The Packing Configuration Has Been Updated"
        )

        return super().form_valid(form)


class UpdateRunView(PermissionRequiredMixin, UpdateView):
    """
    View to Edit a Run.
    """
    permission_required = "packing.edit_run"
    model = Run
    template_name = "update/update-run.html"
    fields = "__all__"
    success_url = reverse_lazy("search-runs")

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS,
            "The Run Has Been Updated")

        return super().form_valid(form)


class UpdatePackingView(PermissionRequiredMixin, UpdateView):
    """
    View to Edit a Run already assigned to a Week Plan.
    """
    permission_required = "packing.edit_packingrun"
    model = PackingRun
    template_name = "update/update-packing-run.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse('plan-detail', kwargs={'pk': self.object.week_id})

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS, "The Packing Run Has Been Updated"
        )

        return super().form_valid(form)


# _______________DELETE VIEWS_______________


class DeletePlanView(PermissionRequiredMixin, DeleteView):
    """
    View to Delete a Week Plan.
    """
    permission_required = "packing.delete_week"
    model = Week
    template_name = "delete/delete.html"
    fields = "__all__"
    success_url = reverse_lazy("search-plans")

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS, "The Plan Has Been Deleted"
        )

        return super().form_valid(form)


class DeleteProductView(PermissionRequiredMixin, DeleteView):
    """
    View to Delete a Product.
    """
    permission_required = "packing.delete_product"
    model = Product
    template_name = "delete/delete-product.html"
    fields = "__all__"
    success_url = reverse_lazy("search-products")

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS, "The Product Has Been Deleted"
        )

        return super().form_valid(form)


class DeletePackagingView(PermissionRequiredMixin, DeleteView):
    """
    View to Delete a Packaging Configuration.
    """
    permission_required = "packing.delete_pack"
    model = Pack
    template_name = "delete/delete-packaging.html"
    fields = "__all__"
    success_url = reverse_lazy("search-packaging")

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS,
            "The Packing Configuration Has Been Deleted"
        )

        return super().form_valid(form)


class DeleteRunView(PermissionRequiredMixin, DeleteView):
    """
    View to Delete a Run.
    """
    permission_required = "packing.delete_run"
    model = Run
    template_name = "delete/delete-run.html"
    fields = "__all__"
    success_url = reverse_lazy("search-runs")

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS,
            "The Run Has Been Deleted")

        return super().form_valid(form)


class DeletePackingView(PermissionRequiredMixin, DeleteView):
    """
    View to remove an assigned Run from a Week Plan.
    """
    permission_required = "packing.delete_packing_run"
    model = PackingRun
    template_name = "delete/delete-packing-run.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse('plan-detail', kwargs={'pk': self.object.week_id})

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS, "The Packing Run Has Been Deleted"
        )

        return super().form_valid(form)
