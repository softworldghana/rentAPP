from django import forms
from expenditure.models import expenditure

    
class expenditure_date(forms.DateInput):
    input_type = 'date'


class new_expenseForm(forms.ModelForm):
    expenditure_date = forms.DateField(widget=expenditure_date)

    class Meta:        
        model = expenditure
        fields = [
            'expenditure_date',
            'expenditure_purpose',
            'expenditure_beneficiary',
            'expenditure_amount',
            'expenditure_group_no'
        ]
