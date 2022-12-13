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

# ________________________Search Views________________________


def search_plans(request):
    """
    This view is the search nexus for all Week Plans.
    In this view plans show up as cards below the search bar
    and CRUD functionality is made available to the user.
    """
    qs = Week.objects.all()
    week_search_query = request.GET.get("search-query")

    # filter objects to display only those relevant to search parameter
    if week_search_query != "" and week_search_query is not None:
        qs = qs.filter(name__icontains=week_search_query)

    context = {
        "queryset": qs,
    }

    return render(request, "search/search-plans.html", context)


# __________________________________________________________________
def search_products(request):
    """
    This view is the search nexus for all Products.
    In this view Products show up as cards below the search bar
    and CRUD functionality is made available to the user.
    """
    qs = Product.objects.all()
    product_search_query = request.GET.get("search-query")

    # filter objects to display only those relevant to search parameter
    if product_search_query != "" and product_search_query is not None:
        qs = qs.filter(
            Q(name__icontains=product_search_query)
            | Q(customer__icontains=product_search_query)
        )

    context = {
        "queryset": qs,
    }
    return render(request, "search/search-products.html", context)


# __________________________________________________________________
def search_packaging(request):
    """
    This view is the search nexus for all Packaging Configurations.
    In this view Packing Configs show up as cards below the search bar
    and CRUD functionality is made available to the user.
    """
    qs = Pack.objects.all()
    pack_search_query = request.GET.get("search-query")

    # filter objects to display only those relevant to search parameter
    if pack_search_query != "" and pack_search_query is not None:
        qs = qs.filter(name__icontains=pack_search_query)

    context = {
        "queryset": qs,
    }
    return render(request, "search/search-packaging.html", context)


# __________________________________________________________________
def search_runs(request):
    """
    This view is the search nexus for all Runs.
    In this view Runs show up as cards below the search bar
    and CRUD functionality is made available to the user.
    """
    qs = Run.objects.all()
    run_search_query = request.GET.get("search-query")

    # filter objects to display only those relevant to search parameter
    if run_search_query != "" and run_search_query is not None:
        qs = qs.filter(name__icontains=run_search_query)

    context = {
        "queryset": qs,
    }
    return render(request, "search/search-runs.html", context)


# _________________________CREATE VIEWS__________________________
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
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS, "The Plan Has Been Created"
        )

        return super().form_valid(form)


# __________________________________________________________________
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
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS, "The Product Has Been Created"
        )

        return super().form_valid(form)


# __________________________________________________________________
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
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS, "The Packing Configuration Has Been Created"
        )

        return super().form_valid(form)


# __________________________________________________________________
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
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(self.request, messages.SUCCESS, "The Run Has Been Created")

        return super().form_valid(form)


# __________________________________________________________________
class CreatePackingView(PermissionRequiredMixin, CreateView):
    """
    View to assign a Packing Run to a Week Plan.
    """

    permission_required = "packing.create_packingrun"
    model = PackingRun
    fields = [
        "name",
        "week",
        "team",
        "day",
        "time",
        "notes",
    ]
    template_name = "create/create-packing-run.html"

    # week automatically selected when create form loaded.
    def get_initial(self):
        initial = super(CreatePackingView, self).get_initial()
        initial["week"] = Week.objects.get(pk=self.kwargs["pk"])
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["week"] = Week.objects.get(pk=self.kwargs["pk"])
        return context

    # redirect to original plan detail page.
    def get_success_url(self):
        return reverse("plan-detail", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        form.instance.created_by = self.request.user
        messages.add_message(
            self.request, messages.SUCCESS, "The Packing Run Has Been Created"
        )

        return super().form_valid(form)


# ___________________Live Plan Create View_________________________________
class CreateLivePackingView(PermissionRequiredMixin, CreateView):
    """
    View to assign a Packing Run to a Week Plan.
    """

    permission_required = "packing.create_packingrun"
    model = PackingRun
    fields = [
        "name",
        "week",
        "team",
        "day",
        "time",
        "notes",
    ]
    template_name = "create/create-packing-run.html"

    # week automatically selected when create form loaded.
    def get_initial(self):
        initial = super(CreateLivePackingView, self).get_initial()
        initial["week"] = Week.objects.get(pk=self.kwargs["pk"])
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["week"] = Week.objects.get(pk=self.kwargs["pk"])
        return context

    # redirect to original plan detail page.
    def get_success_url(self):
        return reverse("live-plan")

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        form.instance.created_by = self.request.user
        messages.add_message(
            self.request, messages.SUCCESS, "The Packing Run Has Been Created"
        )

        return super().form_valid(form)


# _________________________DETAIL VIEWS___________________________
class DetailPlanView(DetailView):
    """
    This View can be accessed from the plan search page and displays
    reports about a given plan.
    """

    model = Week
    template_name = "detail/plan-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        week = Week.objects.get(id=pk)
        runs = PackingRun.objects.filter(week__id=pk).get_calcs()
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


# _________________Live Custom Detail ____________________________
def live_plan(request):
    """
    This view is the main dashboard view for a week plan and will
    display only if status is 'Current'.
    It contains report tables with relevant information for
    staff directly involved in the packing process.
    """
    week = Week.objects.get(status=1)
    runs = PackingRun.objects.filter(week=week).get_calcs()
    notes = runs.exclude(notes__isnull=True)
    team_times = runs.get_team_times(week.id)
    team_day_times = runs.get_team_day_times(week.id)
    context = {
        "runs": runs,
        "tt": team_times,
        "tdt": team_day_times,
        "week": week,
        "notes": notes,
    }

    return render(request, "detail/live-plan-detail.html", context)


# _________________________UPDATE VIEWS_________________________
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
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS, "The Plan Has Been Updated"
        )

        return super().form_valid(form)


# __________________________________________________________________
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
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS, "The Product Has Been Updated"
        )

        return super().form_valid(form)


# __________________________________________________________________
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
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS, "The Packing Configuration Has Been Updated"
        )

        return super().form_valid(form)


# __________________________________________________________________
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
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(self.request, messages.SUCCESS, "The Run Has Been Updated")

        return super().form_valid(form)


# __________________________________________________________________
class UpdatePackingView(PermissionRequiredMixin, UpdateView):
    """
    View to Edit a Run already assigned to a Week Plan.
    """

    permission_required = "packing.edit_packingrun"
    model = PackingRun
    template_name = "update/update-packing-run.html"
    fields = ["name", "week", "team", "day", "time", "notes", "complete"]

    def get_success_url(self):
        return reverse("plan-detail", kwargs={"pk": self.object.week_id})

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS, "The Packing Run Has Been Updated"
        )

        return super().form_valid(form)


# __________________________________________________________________
class UpdateLivePackingView(PermissionRequiredMixin, UpdateView):
    """
    View to Edit a Run already assigned to a Week Plan.
    """

    permission_required = "packing.edit_packingrun"
    model = PackingRun
    template_name = "update/update-packing-run.html"
    fields = ["name", "week", "team", "day", "time", "notes", "complete"]

    def get_success_url(self):
        return reverse("live-plan")

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS, "The Packing Run Has Been Updated"
        )

        return super().form_valid(form)


# __________________________DELETE VIEWS___________________________
class DeletePlanView(PermissionRequiredMixin, DeleteView):
    """
    View to Delete a Week Plan. Currently not in use, but could be implemented in
    the future if required.
    """

    permission_required = "packing.delete_week"
    model = Week
    template_name = "delete/delete-plan.html"
    fields = "__all__"
    success_url = reverse_lazy("search-plans")

    def delete(self, request, *args, **kwargs):
        """
        Custom delete function adding a success message for display.
        """
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "The selected plan has been successfully deleted",
        )

        return super(DeletePlanView, self).delete(request, *args, **kwargs)


# __________________________________________________________________
class DeleteProductView(PermissionRequiredMixin, DeleteView):
    """
    View to Delete a Product.
    """

    permission_required = "packing.delete_product"
    model = Product
    template_name = "delete/delete-product.html"
    fields = "__all__"
    success_url = reverse_lazy("search-products")

    def delete(self, request, *args, **kwargs):
        """
        Custom delete function adding a success message for display.
        """
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "The selected product has been successfully deleted",
        )

        return super(DeleteProductView, self).delete(request, *args, **kwargs)


# __________________________________________________________________
class DeletePackagingView(PermissionRequiredMixin, DeleteView):
    """
    View to Delete a Packaging Configuration.
    """

    permission_required = "packing.delete_pack"
    model = Pack
    template_name = "delete/delete-packaging.html"
    fields = "__all__"
    success_url = reverse_lazy("search-packaging")

    def delete(self, request, *args, **kwargs):
        """
        Custom delete function adding a success message for display.
        """
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "The selected packing config has been successfully deleted",
        )

        return super(DeletePackagingView, self).delete(request, *args, **kwargs)


# __________________________________________________________________
class DeleteRunView(PermissionRequiredMixin, DeleteView):
    """
    View to Delete a Run.
    """

    permission_required = "packing.delete_run"
    model = Run
    template_name = "delete/delete-run.html"
    fields = "__all__"
    success_url = reverse_lazy("search-runs")

    def delete(self, request, *args, **kwargs):
        """
        Custom delete function adding a success message for display.
        """
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "The selected run has been successfully deleted",
        )

        return super(DeleteRunView, self).delete(request, *args, **kwargs)


# __________________________________________________________________
class DeletePackingView(PermissionRequiredMixin, DeleteView):
    """
    View to remove an assigned Run from a Week Plan.
    """

    permission_required = "packing.delete_packingrun"
    model = PackingRun
    template_name = "delete/delete-packing-run.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("plan-detail", kwargs={"pk": self.object.week_id})

    def delete(self, request, *args, **kwargs):
        """
        Custom delete function adding a success message for display.
        """
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "The selected run has been successfully removed from this plan",
        )

        return super(DeletePackingView, self).delete(request, *args, **kwargs)


# ______________________Live Plan Delete___________________________
class DeleteLivePackingView(PermissionRequiredMixin, DeleteView):
    """
    View to remove an assigned Run from a the Live Plan.
    """

    permission_required = "packing.delete_packingrun"
    model = PackingRun
    template_name = "delete/delete-packing-run.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("live-plan")

    def delete(self, request, *args, **kwargs):
        """
        Custom delete function adding a success message for display.
        """
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "The selected run has been successfully removed from this plan",
        )

        return super(DeleteLivePackingView, self).delete(request, *args, **kwargs)
