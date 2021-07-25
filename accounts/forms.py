from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    # Check if username is not exists
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__exact=username)
        if qs.exists():
            raise forms.ValidationError("This username is already in use. Please pick another.")
        return username

    # Check if email is not exists
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__exact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    # Check if password is same as confirm password
    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Your password and confirmation password do not match. Please try again.")
        # clean(self) function doesnt need return


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
