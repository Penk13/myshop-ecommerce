from django import forms
from django.forms import Textarea, TextInput, DateInput, FileInput
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from .models import Profile

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email'}),
    )
    password1 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Password', 'type': 'password'}),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Confirm Password', 'type': 'password'}),
    )

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
    # Method 1
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['bio'].widget.attrs.update({'rows': 5, 'placeholder': 'Bio'})
    #     self.fields['address'].widget.attrs.update({'placeholder': 'Address'})
    #     self.fields['birth_date'].widget.attrs.update({'type': 'date'})
    #     self.fields['profile_pic'].widget.attrs.update()

    # Method 2
    # bio = forms.CharField(
    #     label="",
    #     widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Bio'}),
    #     required=False,
    # )
    # address = forms.CharField(
    #     label="",
    #     widget=forms.TextInput(attrs={'placeholder': 'Address'}),
    # )
    # birth_date = forms.DateField(
    #     label="",
    #     widget=forms.DateInput(attrs={'type': 'date'}),
    # )
    # profile_pic = forms.ImageField(
    #     label="",
    #     widget=forms.FileInput(),
    # )

    # Method 3
    class Meta:
        model = Profile
        fields = ['bio', 'address', 'birth_date', 'profile_pic']
        widgets = {
            'bio': Textarea(attrs={'rows': 5, 'placeholder': 'Bio'}),
            'address': TextInput(attrs={'placeholder': 'Address'}),
            'birth_date': DateInput(attrs={'type': 'date'}),
            'profile_pic': FileInput(),
        }
        labels = {
            'bio': '',
            'address': '',
            'birth_date': '',
            'profile_pic': '',
        }

# Notes: 
# clean(self) function doesnt need return
