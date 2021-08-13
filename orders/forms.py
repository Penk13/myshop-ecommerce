from django import forms


class CreateOrderForm(forms.Form):
    address = forms.CharField(
        label="<strong> Address </strong>",
        widget=forms.TextInput(attrs={'placeholder': "Where can we ship this item to you?"}),
    )
    quantity = forms.IntegerField(
        label="<strong> Quantity </strong>",
        widget=forms.TextInput(attrs={'placeholder': 'How much do you want to buy?'}),
    )

    def __init__(self, *args, **kwargs):
        product = kwargs.pop("products") or None
        super().__init__(*args, **kwargs)
        # Get the product so we can modify it in clean method
        self.products = product

    def clean_quantity(self):
        product = self.products
        quantity = self.cleaned_data.get("quantity")
        print(product.price)
        print(quantity)
        if not isinstance(quantity, int):
            raise forms.ValidationError("Please enter the correct number")
        if quantity <= 0:
            raise forms.ValidationError("Please enter the correct number")
        if not product.available():
            raise forms.ValidationError("Sorry this item is out of stock, please try again later...")
        if quantity > product.stock:
            raise forms.ValidationError("Sorry this item only has " + str(product.stock) + " pieces left")
        if product.price * quantity >= 9999999999:
            raise forms.ValidationError("Sorry your order is very expensive, try to separate it into 2 or more orders. Thanks")
        return quantity
