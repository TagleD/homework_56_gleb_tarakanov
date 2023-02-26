from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'balance', 'coast')
        labels = {
            'name': 'Наименование продукта',
            'description': 'Описание продукта',
            'image': 'URL картинки',
            'category': 'Выберите категорию из списка',
            'balance': 'Введите остаток товара',
            'coast': 'Цена товара'
        }

        def clean_name(self):
            name = self.cleaned_data.get('name')
            if len(name) < 2:
                raise ValidationError('Наименование должен быть длинее 2-ух символов')
            return name