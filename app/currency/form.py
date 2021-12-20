from django import forms
from currency.models import Rate
from currency.models import Rate2


class RateForms(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            "name",
            "surname",
            "salary",
            "state",
            "child",
            # "date",
        )


class Rate2Forms(forms.ModelForm):
    class Meta:
        model = Rate2
        fields = (
            "sale",
            "buy",
            "source",
            # "created",
            "type",
        )
