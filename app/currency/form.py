from django import forms
from currency.models import Rate


class RateForms(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            "name",
            "surname",
            "salary",
            "state",
            "child",
        )
