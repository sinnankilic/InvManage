from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    
      class Meta:
            model = Product
            fields = '__all__'
            labels={
                  'product_id':'Prodcut_Id',
                  'name':'Name',
                  'sku':'Sku',
                  'price':'Price',
                  'quantity':'Quantity',
                  'supplier':'Supplier',
            }

            widgets={

                  'product_id': forms.HiddenInput(),
                  'name':forms.TextInput(
                        attrs={'placeholder':'örn. jeans','class':'form-control'}),
                  'sku':forms.TextInput(
                        attrs={'placeholder':'örn. SK123','class':'form-control'}),
                  'price':forms.NumberInput(
                        attrs={'placeholder':'örn. 52.5','class':'form-control'}),
                  'quantity':forms.NumberInput(
                        attrs={'placeholder':'örn. 127','class':'form-control'}),
                  'supplier':forms.TextInput(
                        attrs={'placeholder':'örn. Sinnk Co.','class':'form-control'}),
                 
            }
            




