from . import views
from django.urls import path


urlpatterns = [
    # _______________LISTS_______________
    # plan list
    path('plan/', views.PlanView.as_view(), name='plan-list'),
    # product list
    path('product/', views.ProductView.as_view(), name='product-list'),
    # packaging list
    path('packaging/', views.PackagingView.as_view(), name='packaging-list'),
    # run list
    path('run/', views.RunView.as_view(), name='run-list'),
    # packing-run list
    path('packing-run/', views.PackingRunView.as_view(), name='packing-run-list'),
    # _______________CREATE_______________
    # plan create
    path('plan/create/', views.CreatePlanView.as_view(), name='plan-create'),
    # product create
    path('product/create/', views.CreateProductView.as_view(), name='product-create'),
    # packaging create
    path('packaging/create/', views.CreatePackagingView.as_view(), name='packaging-create'),
    # run create
    path('run/create/', views.CreateRunView.as_view(), name='run-create'),
    # packing-run create
    path('packing-run/create/', views.CreatePackingView.as_view(), name='packing-run-create'),
]