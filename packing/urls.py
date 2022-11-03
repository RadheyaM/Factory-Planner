from . import views
from django.urls import path


urlpatterns = [
    # plan list
    path('plans/', views.PlanView.as_view(), name='plan-list'),
    # product list
    path('products/', views.ProductView.as_view(), name='product-list'),
    # packaging list
    path('packaging/', views.PackagingView.as_view(), name='packaging-list'),
    # run list
    path('run/', views.RunView.as_view(), name='run-list'),
    # packing run list
    path('packing-run/', views.PackingRunView.as_view(), name='packing-run-list'),
]