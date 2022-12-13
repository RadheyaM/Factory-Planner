from django.contrib.auth.decorators import login_required
from . import views
from django.urls import path


urlpatterns = [
    # Home is set to search_plans to avoid any errors linked to plan status.
    path("", login_required(views.search_plans), name="home"),

    # _______________SEARCH VIEWS_______________
    path(
        "search/products", login_required(views.search_products), name="search-products"
    ),
    path(
        "search/plans",
        login_required(views.search_plans),
        name="search-plans"),
    path(
        "search/packaging",
        login_required(views.search_packaging),
        name="search-packaging",
    ),
    path(
        "search/runs",
        login_required(views.search_runs),
        name="search-runs"
    ),
    # _______________DETAIL_______________
    path(
        "plan/<int:pk>/detail",
        views.login_required(views.DetailPlanView.as_view()),
        name="plan-detail",
    ),
    # Live plan custom detail view
    path(
        "plan/live-plan",
        login_required(views.live_plan),
        name="live-plan",
    ),
    # _______________CREATE_______________
    # plan create
    path(
        "plan/create/",
        login_required(views.CreatePlanView.as_view()),
        name="plan-create",
    ),
    # product create
    path(
        "product/create/",
        login_required(views.CreateProductView.as_view()),
        name="product-create",
    ),
    # packaging create
    path(
        "packaging/create/",
        login_required(views.CreatePackagingView.as_view()),
        name="packaging-create",
    ),
    # run create
    path(
        "run/create/",
        login_required(views.CreateRunView.as_view()),
        name="run-create"
    ),
    # packing-run create
    path(
        "packing-run/create/<int:pk>",
        login_required(views.CreatePackingView.as_view()),
        name="packing-run-create",
    ),
    # live-packing-run create
    path(
        "live-packing-run/create/<int:pk>",
        views.login_required(views.CreateLivePackingView.as_view()),
        name="live-packing-run-create",
    ),
    # _______________UPDATE_______________
    # plan update
    path(
        "plan/<int:pk>/update/",
        login_required(views.UpdatePlanView.as_view()),
        name="plan-update",
    ),
    # product update
    path(
        "product/<int:pk>/update/",
        views.login_required(views.UpdateProductView.as_view()),
        name="product-update",
    ),
    # packaging update
    path(
        "packaging/<int:pk>/update/",
        login_required(views.UpdatePackagingView.as_view()),
        name="packaging-update",
    ),
    # run update
    path(
        "run/<int:pk>/update/",
        login_required(views.UpdateRunView.as_view()),
        name="run-update",
    ),
    # packing-run update
    path(
        "packing-run/<int:pk>/update/",
        login_required(views.UpdatePackingView.as_view()),
        name="packing-run-update",
    ),
    # live-packing-run update
    path(
        "live-packing-run/<int:pk>/update/",
        login_required(views.UpdateLivePackingView.as_view()),
        name="live-packing-run-update",
    ),
    # _______________DELETE_______________
    # plan delete
    path(
        "plan/<int:pk>/delete/",
        login_required(views.DeletePlanView.as_view()),
        name="plan-delete",
    ),
    # product delete
    path(
        "product/<int:pk>/delete/",
        login_required(views.DeleteProductView.as_view()),
        name="product-delete",
    ),
    # packaging delete
    path(
        "packaging/<int:pk>/delete/",
        login_required(views.DeletePackagingView.as_view()),
        name="packaging-delete",
    ),
    # run delete
    path(
        "run/<int:pk>/delete/",
        login_required(views.DeleteRunView.as_view()),
        name="run-delete",
    ),
    # packing-run delete
    path(
        "packing-run/<int:pk>/delete/",
        login_required(views.DeletePackingView.as_view()),
        name="packing-run-delete",
    ),
    # live-packing-run delete
    path(
        "live-packing-run/<int:pk>/delete/",
        login_required(views.DeleteLivePackingView.as_view()),
        name="live-packing-run-delete",
    ),
]
