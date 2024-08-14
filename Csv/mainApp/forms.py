from django import forms

class ItemSearchForm(forms.Form):
    item_name = forms.CharField(required=False, label='Item Name')
    item_code = forms.CharField(required=False, label='Item Code')
    vendor_name = forms.CharField(required=False, label='Vendor Name')
