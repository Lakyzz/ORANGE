from django import forms
from .models import Product


class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ['name','price','description','image_product']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'image_product':forms.ClearableFileInput,
        }