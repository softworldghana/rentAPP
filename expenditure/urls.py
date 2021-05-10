from django.urls import path
from . import views

urlpatterns = [
    path('', views.expenses),
    path('new/', views.new_expense, name='new_expense'),
    path('edit/<expense_id>', views.expense_update, name='expense_update'),
    path('delete/<expense_id>', views.expense_delete, name='expense_delete'),
]