from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = [
            "title",
            "amount",
            "category",
            "description",
            "date",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. College lunch",
                }
            ),
            "amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter amount",
                    "step": "0.01",
                    "min": "0",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Add a short description...",
                    "rows": 4,
                }
            ),
            "date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
        }
