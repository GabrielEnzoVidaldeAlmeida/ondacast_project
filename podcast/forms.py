from django import forms
from .models import Episodio, Podcast

class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields= ['nome','descricao','foto']

class EpisodioForm(forms.ModelForm):
    class Meta:
        model = Episodio
        fields = ['titulo', 'descricao', 'capa', 'arquivo_audio', 'podcast']
        widgets = {
            'descricao': forms.TextInput(attrs={'maxlength': 140}),
        }

class EditarPodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ['nome', 'descricao', 'foto']
        widgets = {
            'descricao': forms.TextInput(attrs={'maxlength': 140}),
        }

class ExcluirEpisodioForm(forms.ModelForm):
    episodio_id = forms.IntegerField(widget=forms.HiddenInput())