from django import forms
from .models import PackingRun


class PackingRunForm(forms.ModelForm):
    """
    Form used with crispy forms to improve styling.
    """
    class Meta:
        model = PackingRun
        fields = '__all__'
