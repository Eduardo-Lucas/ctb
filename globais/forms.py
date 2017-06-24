from django import forms

from .models import GlobEmpresas


class GlobEmpresasForm(forms.ModelForm):
    class Meta:
        model = GlobEmpresas
        fields = '__all__'
