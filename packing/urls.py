from . import views
from django.urls import path


urlpatterns = [
    # plan list
    path('plan/', views.PlanView.as_view(), name='plan-list')
]