# catalog/forms.py

from django import forms
from django.core.exceptions import ValidationError
from .models import Product

FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]

class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = [
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар',
    ]

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        for word in self.FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f'Запрещённое слово в названии: "{word}"')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        for word in self.FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f'Запрещённое слово в описании: "{word}"')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price
