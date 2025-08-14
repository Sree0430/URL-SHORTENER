from django import forms
from .models import ShortURL

class ShortenForm(forms.Form):
    long_url = forms.URLField(
        label='Long URL',
        widget=forms.URLInput(attrs={'class':'form-control','placeholder':'Enter your long URL'})
    )
    custom = forms.SlugField(
        label='Custom code (optional)',
        required=False,
        max_length=16,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Custom short code (optional)'}),
    )

    def clean_custom(self):
        c = self.cleaned_data.get('custom')
        if c and ShortURL.objects.filter(code=c).exists():
            raise forms.ValidationError("This code is already taken.")
        return c
