from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def login(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('jobs')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Invalid username')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request, "username or password is invalid")
    return render(request,'users/login.html')

def logout(request):
    logout(request)
    messages.info(request,'user was logged out')
    return redirect (login)


from .forms import CustomUserCreationForm
def register(request):
    page = 'register'
    form = CustomUserCreationForm(request.POST)

    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = user.username
            user.save()

            messages.success(request, 'User account was created')
            login(request,user)
            return redirect(request, 'login')
        else:
            messages.error(request,'an error occurred during registration')
    context = {
        'page': page,
        'form': form
        }
    return render(request, 'users/register.html',context)


