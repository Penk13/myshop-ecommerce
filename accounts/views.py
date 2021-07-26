from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.auth.models import Group

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

        group = Group.objects.get(name='customer')

        # form.save() ---> It's only for ModelForm
        # Create user and add to group
        try:
            user = User.objects.create_user(username, email, password)
            group.user_set.add(user)
        except:
            user = None
        if user is not None:
            # TODO try authenticate()
            login(request, user)
            return redirect('products:homepage')
        else:
            message = "Registration failed ..."
            return render(request, "accounts/error_page.html", {"message": message})
    return render(request, "accounts/register_page.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products:homepage')
        else:
            message = "Login failed ..."
            return render(request, "accounts/error_page.html", {"message": message})
    return render(request, "accounts/login_page.html", {"form": form})


def logout(request):
    logout(request)
    return redirect("accounts:login")
