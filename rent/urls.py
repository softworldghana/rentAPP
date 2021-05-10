from django.urls import path
from . import views

urlpatterns = [
    path('', views.rent),
    path('new_rent/', views.new_rent),
    path('edit/<rent_id>', views.rent_update, name='rent_update'),
    path('delete/<rent_id>', views.rent_delete, name='rent_delete'),
]