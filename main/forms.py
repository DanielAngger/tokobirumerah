from django.forms import ModelForm
from main.models import PesananEntry

class PesananEntryForm(ModelForm):
    class Meta:
        model = PesananEntry
        fields = ["pesanan", "keterangan", "quantitas"]