from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request, 'main/about.html')
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        if User.is_authenticated:
            return redirect('home')
        username = request.POST.get('username')
        password = request.POST.get('password')
        userr=auth.authenticate(request, username=username, password=password)
        if userr is not None:
            auth.login(request, userr)
            return redirect('home')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, 'main/login.html')  # Render the login template