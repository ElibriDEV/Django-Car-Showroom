import datetime as dt

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from users.forms import AuthUserForm, UserRegistrationForm


class Login(LoginView):
    fields = ["username", "password"]
    template_name = "users/login.html"
    form_class = AuthUserForm


class Logout(LogoutView):
    template_name = "users/logout.html"


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            reg_f = form.save(commit=False)
            reg_f.is_active = True
            reg_f.is_staff = False
            reg_f.is_superuser = False
            reg_f.date_joined = dt.datetime.now()
            reg_f.last_login = dt.datetime.now()
            reg_f.save()

            reg_f.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, reg_f)
            return redirect("main:index")
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})
