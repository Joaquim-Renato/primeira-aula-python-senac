from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import User

def login_user(request):
    if request.method == "post": 
        userName = request.post["email"]
        userPassword = request.post["password"]
        try:
            success = User.objects.get(user = userName, password = userPassword)
            request.session["userID"] = success.id
            return redirect("home")
        except:
            User.DoesNotExist
            messages.error("usuario e/ou senha inválidos!")
    return render(request, "index.html")

def logout_user(request):
    return

def check_login(request):
    if "userID" in request.session:
        return render(request, "home.html")
    else:
        return redirect("index")
    
