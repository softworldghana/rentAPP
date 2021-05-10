from django.shortcuts import render, redirect, get_object_or_404
from rent.models import Rent
from .forms.new_rentForm import new_rentForm
from datetime import datetime


def new_rent(request):
    form = new_rentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # rent_duration = abs((datetime.strptime(form.cleaned_data['duration_to'], "%Y-%m-%d") - datetime.strptime(form.cleaned_data['duration_from'], "%Y-%m-%d")).months)
            # total_rent = rent_duration * form.cleaned_data['rent_per_month']
            
            # from datetime import datetime
            # def days_between(d1, d2):
            # d1 = datetime.strptime(d1, "%Y-%m-%d")
            # d2 = datetime.strptime(d2, "%Y-%m-%d") 
            # return abs((d2 - d1).days)

            form.save()
            r_id = form.auto_id()
            # new_order = Sales_h(total_rent=total_rent)
            # new_order.update()
            # return redirect('book_list')
            return render(request, 'new_rent.html', {'form': form})
    return render(request, 'new_rent.html', {'form': form})


def rent(request):
    rent = Rent.objects.all()
    return render(request, 'rent.html', {'rent': rent})


def rent_delete(request, rent_id):
    rent = get_object_or_404(Rent, pk=rent_id)    
    if request.method == 'POST':
        rent.delete()
        rent = Rent.objects.all()
        return render(request, 'rent.html', {'rent': rent})
    rent = Rent.objects.all()
    return render(request, 'rent.html', {'rent': rent})


def rent_update(request, rent_id):
    rent = get_object_or_404(Rent, pk=rent_id)    
    form = new_rentForm(request.POST or None, instance=rent)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            rent = Rent.objects.all()
            return render(request, 'rent.html', {'rent': rent})
    return render(request, 'new_rent.html', {'form': form})
