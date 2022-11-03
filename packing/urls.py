from . import views
from django.urls import path


urlpatterns = [
    # plan list
    path('plans/', views.PlanView.as_view(), name='plan-list'),
    # product list
    path('products/', views.ProductView.as_view(), name='product-list'),
    # packaging list
    path('packaging/', views.PackagingView.as_view(), name='packaging-list'),
]