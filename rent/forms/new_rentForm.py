from django import forms
from rent.models import Rent


class date_from(forms.DateInput):
    input_type = 'date'


class date_to(forms.DateInput):
    input_type = 'date'


class new_rentForm(forms.ModelForm):
    duration_from = forms.DateField(widget=date_from)
    duration_to = forms.DateField(widget=date_to)

    class Meta:
        model = Rent
        fields = [
            'tenant_name',
            'property_name',
            'room_types',
            'duration_from',
            'duration_to',
            'rent_per_month',
            # 'total_rent',
            'deposit_amt'
        ]

