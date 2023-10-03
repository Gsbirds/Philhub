from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.forms import SignUpForm
from accounts.forms import LogInForm
from .encoders import LogInEncoder
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            if password == password_confirmation:
                user = User.objects.create_user(
                    username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )

                login(request, user)

                return redirect("show_page")
    else:
        form = SignUpForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


@require_http_methods(["POST"])
def user_login(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )
            # if user is not None:
            #     login(request, user)
            #     return redirect("show_page")

            content = json.loads(request.body)
            user = LogInForm.objects.create(**content)
            return JsonResponse(
                user,
                encoder=LogInEncoder,
                safe=False,
            )


#         form= LogInForm()
#     context = {
#         "form":form,
#     }

#     return render(request, "accounts/login.html", context)

# def user_logout(request):
#     logout(request)
#     return redirect("show_page")
