from django import apps
from django import forms
from .models import Playlist

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'songs']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'search-input', 'style': 'border-bottom: 1px solid #000; width: 100%;'}),
            'songs': forms.CheckboxSelectMultiple(), 
        }

    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("The name of the playlist has to contain at least 2 digits.")

        PAROLE_PROIBITE =[
            'fuck' ,
            'fanculo' ,
            'bitch' ,
            'stronzo' ,
        ]    
        name_lower = name.lower()

        for parola in PAROLE_PROIBITE:
            if parola in name_lower:
                raise forms.ValidationError("The name of the playlist contains offensive words.")
        
        return name
