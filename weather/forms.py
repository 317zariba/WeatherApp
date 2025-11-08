from django import forms

class CityForm(forms.Form):
    city_name = forms.CharField(
        label = '',
        max_length = 100,
        widget = forms.TextInput(attrs={
            'placeholder': 'Введите город...',
            'class': 'form-control'
                    
                })
    )