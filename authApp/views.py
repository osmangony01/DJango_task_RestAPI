from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# @login_required(login_url="login")
# Create your views here.

def register(request):

    if request.method == "POST":
        first_name = request.POST.get('fname') 
        last_name = request.POST.get('lname') 
        username = request.POST.get('uname') 
        email = request.POST.get('email') 
        password = request.POST.get('pass1') 
		#password2 = request.POST.get('pass2')
        print(first_name, last_name, username, email, password, )
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        return redirect('login')

    return render(request, 'auth/register.html') 
    

def login(request):
	if request.method == "POST":
		username = request.POST.get('uname')
		password = request.POST.get('pass')
		print(username,password)
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth_login(request, user)
			return redirect('home') 
		else:
			return redirect('login')

	return render(request, 'auth/login.html')

def logoutPage(request):
	logout(request)
	return redirect('login')