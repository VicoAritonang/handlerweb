from django import forms
from .models import Formulir

class FormulirForm(forms.ModelForm):
    class Meta:
        model = Formulir
        fields = ['nama', 'nomor', 'deskripsi', 'jenis_usaha', 'omzet']
        widgets = {
            'deskripsi': forms.Textarea(attrs={'rows': 4}),
        }

    # Validasi khusus untuk field nomor
    def clean_nomor(self):
        nomor = self.cleaned_data.get('nomor')
        if not (9 <= len(str(nomor)) <= 13):
            raise forms.ValidationError("Nomor telepon harus memiliki panjang 9 hingga 13 angka.")
        return nomor
