from django import forms


class CreateOrderForm(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Where can we ship this item to you?"}))
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How much do you want to buy?'}))
