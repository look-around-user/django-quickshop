from django import forms

class BuydetailForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    quantity = forms.IntegerField(label='Quantity')

class ShoplistForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
