from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Product_Family


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'category', 'product_family', 'name', 'SKU', 'image', 
             'product_size', 'pack', 'price', 'description', 'active',
        )

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        cat_names = [(c.id, c.get_name()) for c in categories]
        product_families = Product_Family.objects.all()
        pf_names = [(pf.id, pf.get_name()) for pf in product_families]

        self.fields['category'].choices = cat_names
        self.fields['product_family'].choices = pf_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-border rounded-0'


class ProductFamilyForm(forms.ModelForm):

    class Meta:
        model = Product_Family
        fields = '__all__'

