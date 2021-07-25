from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.http import HttpResponse

from .forms import (
    RegisterForm,
    LoginForm,
)

User = get_user_model()


def register_view(request):
    form = RegisterForm(request.POST or None)
    # Call clean function in forms
    if form.is_valid():
        # Get input from user
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")

        # form.save() ---> It's only for ModelForm
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user is not None:
            login(request, user)
            return redirect('accounts:login-view')
        else:
            return HttpResponse("Registration failed ...")
    return render(request, "accounts/register_page.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        # TODO
        print("LOGIN SUCCESSFUL")
    return render(request, "accounts/login_page.html", {"form": form})
