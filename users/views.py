from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products:list')
        else:
            return redirect('users:signin')
    return render(request, 'registration/signin.html')


def signout(request):
    logout(request)
    return redirect('users:signin')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:signin')
    form = UserCreationForm()
    context = {
        "form": form
    }
    return render(request, 'registration/signup.html', context=context)