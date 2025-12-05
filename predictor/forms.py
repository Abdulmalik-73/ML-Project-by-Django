from django import forms

LOCATION_CHOICES = [
    ('Tinika', 'Tinika'),
    ('Harar_gate_area', 'Harar Gate Area'),
    ('University_area', 'University Area'),
    ('Gende_Kore', 'Gende Kore'),
    ('Quncho_Ber', 'Quncho Ber'),
    ('Kore_Hiwot', 'Kore Hiwot'),
]

CONDITION_CHOICES = [
    ('New', 'New'),
    ('Good', 'Good'),
    ('Needs_Renovation', 'Needs Renovation'),
]

class HousePredictionForm(forms.Form):
    bedrooms = forms.IntegerField(
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Number of Bedrooms'
        })
    )
    bathrooms = forms.IntegerField(
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Number of Bathrooms'
        })
    )
    house_size = forms.FloatField(
        min_value=30,
        max_value=500,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'House Size (sqm)',
            'step': '0.1'
        })
    )
    land_size = forms.FloatField(
        min_value=100,
        max_value=2000,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Land Size (sqm)',
            'step': '0.1'
        })
    )
    location = forms.ChoiceField(
        choices=LOCATION_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    condition = forms.ChoiceField(
        choices=CONDITION_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    year_built = forms.IntegerField(
        min_value=2000,
        max_value=2025,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Year Built'
        })
    )
