from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.hashers import make_password, HASHERS
from django.http import HttpResponseRedirect
from django import forms

from customer.models import UserEntity
from customer.forms import RegisterForm, LoginForm

# to do: customer/account


# Create your views here.

def login(request):
	form = LoginForm()
	return render(request, 'login.html', {'form': form,});

def create(request):
	if (request.method == 'POST'):
		form = RegisterForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.password = make_password(form.password)
			form.status = 1
			new_user = form.save()
			return HttpResponseRedirect('/custoemr/account')
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form,})

def loginPost(request):
	if (request.method == 'POST'):
		form = LoginForm(request.POST)
		if form.is_valid():	
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = UserEntity.objects.filter(username__exact=username, password__exact=password)
			# user = auth.authenticate(username=username, password=password)
			if user:
				# auth.login(request, user)
				return HttpResponseRedirect('/customer/account/')
			else:
				return HttpResponseRedirect('/customer/account/invalid')
		# else:
		# 	form = LoginForm()
	return render(request, 'login.html', {'form':form})

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')