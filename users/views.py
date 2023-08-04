from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib import auth
# Create your views here.

def registration(request):
    return render(request, 'registration/main.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        auth.login(request, user)

        return redirect('/')
    return render(request, 'registration/main.html')