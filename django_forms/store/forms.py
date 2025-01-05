from django import forms

from store.models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']
        labels = {
            'name': 'Продукт',
            'description': 'Описание',
            'price': 'Цена',
            'category': 'Категория',
        }
        widgets = {
            'name': forms.TextInput(attrs=
                                    {
                                        'class': 'form-control',
                                        'placeholder': 'Наименование продукта'
                                    }),
            'description': forms.Textarea(attrs=
                                          {
                                              'class': 'form-control',
                                              'rows': 2,
                                              'placeholder': 'Введите описание продукта'
                                          }),
            'price': forms.TextInput(attrs=
                                     {
                                         'class': 'form-control',
                                         'placeholder': 'Укажите цену продукта'
                                     }),
            'category': forms.Select(attrs=
                                     {
                                         'class': 'form-control',
                                         'placeholder': 'Выберите категорию продукта'
                                     }),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Наименование товара не должно быть менее 3-х символов')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 10:
            raise forms.ValidationError('Описание товара не должно быть менее 30-ти символов')
        return description

    def clean_price(self):
        price = round(float(self.cleaned_data['price']), 2)
        if price <= 0:
            raise forms.ValidationError('Цена должна быть положительной')
        return price

    def clean(self):
        cleaned_data = super(ProductForm, self).clean()
        description = cleaned_data.get("description")
        forbidden_words = ['сигареты', 'вино', 'наркотик']
        if description:
            for word in forbidden_words:
                if word in description.lower():
                    raise forms.ValidationError(f'Описание содержит запрещенное слово: {word}')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {
            'name': 'Категория',
            'description': 'Описание'
        }
        widgets = {
            'name': forms.TextInput(attrs=
                                    {
                                        'class': 'form-control',
                                        'placeholder': 'Наименование категории'
                                    }),
            'description': forms.Textarea(attrs=
                                          {
                                              'class': 'form-control',
                                              'rows': 2,
                                              'placeholder': 'Описание категории'
                                          })
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Наименование категории не должно быть менее 3-х символов')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 10:
            raise forms.ValidationError('Описание категории не должно быть менее 10-ти символов')
        return description

    def clean(self):
        cleaned_data = super(CategoryForm, self).clean()
        forbidden_words = ['сигареты', 'вино', 'наркотик', 'алкоголь']

        description = cleaned_data.get("description")
        if description:
            for word in forbidden_words:
                if word in description.lower():
                    raise forms.ValidationError(f'Описание содержит запрещенное слово: {word}')

        name = cleaned_data.get("name")
        if name:
            for word in forbidden_words:
                if word in name.lower():
                    raise forms.ValidationError(f'Наименование содержит запрещенное слово: {word}')
