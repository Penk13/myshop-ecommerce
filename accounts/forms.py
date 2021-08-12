from django import forms
from django.forms import Textarea, TextInput, DateInput, FileInput
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Profile

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

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
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )
    password = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Password', 'type': 'password'}),
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        # Check if user and password is matching and exists
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("This is an invalid user.")


class ProfileForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # self.fields['bio'].widget.attrs.update({'class': 'form-control my-3', 'placeholder': 'Bio'})

    class Meta:
        model = Profile
        fields = ['bio', 'address', 'birth_date', 'profile_pic']
        widgets = {
            'bio': Textarea(attrs={'class': 'form-control my-3', 'rows': 5, 'placeholder': 'Bio'}),
            'address': TextInput(attrs={'class': 'form-control my-3', 'placeholder': 'Address'}),
            'birth_date': DateInput(attrs={'class': 'form-control my-3', 'type': 'date'}),
            'profile_pic': FileInput(attrs={'class': 'form-control my-3'}),
        }
        labels = {
            'bio': '',
            'address': '',
            'birth_date': '',
            'profile_pic': '',
        }
