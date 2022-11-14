from .models import Run
from bootstrap_modal_forms.forms import BSModalModelForm

class RunModelForm(BSModalModelForm):
    class Meta:
        model = Run
        modalID = '#run'
        fields = '__all__'