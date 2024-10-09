from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import User
from django.contrib.auth import logout

def login_user(request):
    if request.method == "POST": 
        userName = request.POST["email"]
        userPassword = request.POST["password"]

        try:
            success = User.objects.get(user = userName, password = userPassword)
            request.session["userID"] = success.id
            return redirect("home")
        except User.DoesNotExist:
            messages.error(request, "usuario e/ou senha inválidos!")
    return render(request, "index.html")

def check_login(request):
    if "userID" in request.session:
        return render(request, "home.html")
    else:
        return redirect("index")
    
def logout_user(request):
        logout(request)
        request.session.flush()
        return redirect("index")
  