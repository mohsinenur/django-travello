from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect("/")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Incorrect credential.")
            return redirect("login")
    else:
        return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name'] 
        email = request.POST['email'] 
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1!=password2:
            messages.info(request, 'Password not matched!')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken!')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already taken!')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
            user.save()
            print('User created')
            return redirect('login')
    else:
        return render(request, 'register.html')
