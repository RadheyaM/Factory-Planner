from . import views
from django.urls import path


urlpatterns = [
    path('', views.search_plans, name='home'),
    #_______________DASHBOARD VIEW_______________
    path('search/products', views.search_products, name='search-products'),
    path('search/plans', views.search_plans, name='search-plans'),
    path('search/packaging', views.search_packaging, name='search-packaging'),
    path('search/runs', views.search_runs, name='search-runs'),
    # _______________DETAIL_______________
    path('plan/<int:pk>/detail', views.DetailPlanView.as_view(), name='plan-detail'),
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
    # _______________UPDATE_______________
    # plan update
    path('plan/<int:pk>/update/', views.UpdatePlanView.as_view(), name='plan-update'),
    # product update
    path('product/<int:pk>/update/', views.UpdateProductView.as_view(), name='product-update'),
    # packaging update
    path('packaging/<int:pk>/update/', views.UpdatePackagingView.as_view(), name='packaging-update'),
    # run update
    path('run/<int:pk>/update/', views.UpdateRunView.as_view(), name='run-update'),
    # packing-run update
    path('packing-run/<int:pk>/update/', views.UpdatePackingView.as_view(), name='packing-run-update'),
    # _______________DELETE_______________
    # plan delete
    path('plan/<int:pk>/delete/', views.DeletePlanView.as_view(), name='plan-delete'),
    # product delete
    path('product/<int:pk>/delete/', views.DeleteProductView.as_view(), name='product-delete'),
    # packaging delete
    path('packaging/<int:pk>/delete/', views.DeletePackagingView.as_view(), name='packaging-delete'),
    # run delete
    path('run/<int:pk>/delete/', views.DeleteRunView.as_view(), name='run-delete'),
    # packing-run delete
    path('packing-run/<int:pk>/delete/', views.DeletePackingView.as_view(), name='packing-run-delete'),
]