from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("login/")
    else:
        form = UserForm()
    return render(request, "registration/signup.html", {"myform" : form})

def login(request):
    if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = auth.authenticate(username = username, password = password)
      if user is not None:
            auth.login(request, user)
            return redirect("home")
      else: 
          messages.error(request, "USER NOT FOUND")
          return redirect("login")
    return render(request, "registration/login.html", {})

def logout(request):
    auth.logout(request)
    return redirect("/home")