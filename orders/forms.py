from django import forms

from .models import Order


class CreateOrderForm(forms.Form):

    # Initialize form fields
    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop("request")
    #     super(CreateOrderForm, self).__init__(*args, **kwargs)
    #     self.fields['user'].initial = self.request.user.username
    #     self.fields['products'].initial = kwargs['instance'].name
    #     self.fields['total_price'].initial = kwargs['instance'].price

    address = forms.CharField()

    # class Meta:
    #     model = Order
    #     fields = ["address"]
        # widgets = {
        #     # Make fields disabled so user cant changed
        #     'user': forms.TextInput(attrs={'disabled': True}),
        #     'products': forms.TextInput(attrs={'disabled': True}),
        #     'total_price': forms.TextInput(attrs={'disabled': True})
        # }

    # def clean_user(self):
    #     user = self.cleaned_data.get('user')
    #     return user

    # def clean_products(self):
    #     products = self.cleaned_data.get('products')
    #     return products

    # def clean_total_price(self):
    #     total_price = self.cleaned_data.get('total_price')
    #     return total_price
