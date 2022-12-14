from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('packing.urls'), name='packing_urls'),
    path('accounts/', include('allauth.urls')),
]

handler404='packing.views.handle_404'
handler403='packing.views.handle_403'
handler500='packing.views.handle_500'