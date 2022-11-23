from django import forms
from .models import PackingRun

class PackingRunForm(forms.ModelForm):
    class Meta:
        model = PackingRun
        fields = '__all__'