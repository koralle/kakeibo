from django import forms
from .models import Balance

class BalanceForm(forms.ModelForm):
  class Meta:
    model = Balance
    fields = ('item_name', 'amount', 'registered_date', 'category', 'balance_type')