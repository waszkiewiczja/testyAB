from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

# Create your views here.

def index(request):
    return render(request, 'users/index.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mojetesty:mojetestyindex')

    return render(request, 'users/login.html')
    



def logoutPage(request):
    logout(request)
    messages.info(request, 'Pomyslnie wylogowano')
    return redirect('mojetesty:mojetestyindex')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('mojetesty:mojetestyindex')

    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Konto stworzone')
            
            login(request, user)
            return redirect('mojetesty:mojetestyindex')

    context = {'form':form}
    return render(request, 'users/register.html', context)


