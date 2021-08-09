from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Confirm Password"}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        # Check if username is not exists
        qs = User.objects.filter(username__exact=username)
        if qs.exists():
            raise forms.ValidationError("This username is already in use. Please pick another.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__exact=email)
        # Check if email is exists
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        # Check if password is same as confirm password
        if password1 != password2:
            raise forms.ValidationError("Your password and confirmation password do not match. Please try again.")
        # clean(self) function doesnt need return


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Password"}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        # Check if user and password is matching and exists
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("This is an invalid user.")
