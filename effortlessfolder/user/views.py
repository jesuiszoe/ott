from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
#회원가입 구현
def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'user/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('/')
        else:
            return render(request, 'user/signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'user/signup.html')
    

#로그인 구현
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'user/login.html', {'error': 'username or password is incorrect.'})

    else:
        return render(request, 'user/login.html')
#로그아웃 구현
def logout(request):
    auth.logout(request)
    return redirect('/')