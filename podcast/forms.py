from django import forms
from .models import Episodio

class EpisodioForm(forms.ModelForm):
    class Meta:
        model = Episodio
        fields = ['titulo', 'descricao', 'capa', 'arquivo_audio']
        widgets = {
            'descricao': forms.TextInput(attrs={'maxlength': 140}),
        }