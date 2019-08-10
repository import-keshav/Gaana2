from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
	if request.method == 'POST':
		username_or_email = request.POST['username_email']
		password = request.POST['password']

		user = auth.authenticate(username=username_or_email, password=password)
		if user is not None:
			request.session['username'] = username_or_email
			return redirect('/')
		messages.info(request, 'Invalid username or password')
		return render(request, 'accounts/login.htm')
	return render(request, 'accounts/login.html')


def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']

		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Username Already Taken')
				return render(request, 'accounts/register.html')
			if User.objects.filter(email=email).exists():
				messages.info(request, 'email already taken')				
				return render(request, 'accounts/register.html')
			user = User.objects.create_user(
				username=username,
				password=password1,
				email=email,
				first_name=first_name,
				last_name=last_name)
			user.save()
			return redirect('/')
		messages.info(request, "Passwords didn't matching")
		return render(request, 'accounts/register.html')
	return render(request, 'accounts/register.html')