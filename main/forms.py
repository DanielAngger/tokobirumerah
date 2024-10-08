from django.forms import ModelForm
from main.models import PesananEntry
from django.utils.html import strip_tags

class PesananEntryForm(ModelForm):
    class Meta:
        model = PesananEntry
        fields = ["pesanan", "keterangan", "quantitas"]

    def clean_pesanan(self):
        pesanan = self.cleaned_data["pesanan"]
        return strip_tags(pesanan)

    def clean_keterangan(self):
        keterangan = self.cleaned_data["keterangan"]
        return strip_tags(keterangan)