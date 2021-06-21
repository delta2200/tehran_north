from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='Title', required=True, widget= forms.TextInput(attrs={'placeholder':'please fill this field.'}) )

    class Meta:
        model = Product
        fields = (
            'title',
            'description',
            'price',
            'technical_desc'
        )

class ProductFormRaw(forms.Form):
    title = forms.CharField(label='Title', required=True, widget= forms.TextInput(attrs={'placeholder':'please fill this field.'}) )
    description = forms.CharField()
    price = forms.DecimalField()
    technical_desc = forms.CharField()

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if not "ali" in title:
            raise forms.ValidationError("please enter the valid title")
        return title