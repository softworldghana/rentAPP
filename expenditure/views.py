from django.shortcuts import render, redirect, get_object_or_404
from .forms.new_expenseForm import new_expenseForm
from .models import expenditure


def expenses(request):
    expenses = expenditure.objects.all()
    return render(request, 'expenses.html', {'expenses':expenses})


def new_expense(request):
    form = new_expenseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'new_expense.html', {'form':form}) 
    return render(request, 'new_expense.html', {'form':form})    


def expense_delete(request, expense_id):
    expense = get_object_or_404(expenditure, pk=expense_id)    
    if request.method == 'POST':
        expense.delete()
        return redirect('expenses')
    return redirect('expenses')


def expense_update(request, expense_id):
    expense = get_object_or_404(expenditure, pk=expense_id)    
    form = new_expenseForm(request.POST or None, instance=expense)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('expenses')
    return render(request, 'new_expense.html', {'form': form})
